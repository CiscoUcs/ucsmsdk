# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging

import ucsgenutils
import ucscoreutils
from ucsexception import UcsException
from ucsconstants import NamingId
from ucssession import UcsSession
from ucsmethodfactory import config_resolve_classes

log = logging.getLogger('ucs')


class UcsHandle(UcsSession):
    """
    Handle class is the user interface point for any Ucs related communication.

    Attributes:
        * ip (str): The IP or Hostname of the UCS Server
        * username (str): The username as configured on the UCS Server
        * password (str): The password as configured on the UCS Server
        * port (int or None): The port number to be used during connection
        * secure (bool or None): True for secure connection, otherwise False
        * proxy (str): The proxy object to be used to connect

    Example:
        handle = UcsHandle("192.168.1.1","admin","password")
        handle = UcsHandle("192.168.1.1","admin","password", secure=True)
        handle = UcsHandle("192.168.1.1","admin","password", secure=False)
        handle = UcsHandle("192.168.1.1","admin","password", port=80)
        handle = UcsHandle("192.168.1.1","admin","password", port=443)
        handle = UcsHandle("192.168.1.1","admin","password", port=100,
                            secure=True)
        handle = UcsHandle("192.168.1.1","admin","password", port=100,
                            secure=False)
    """

    def __init__(self, ip, username, password, port=None, secure=None,
                 proxy=None):
        UcsSession.__init__(self, ip, username, password, port, secure, proxy)
        self.__to_commit = {}

    def set_dump_xml(self):
        """
        Enables the xml request and response to be added to logs.
        """

        self._set_dump_xml()

    def unset_dump_xml(self):
        """
        Disables the xml request and response to be added to logs.
        """

        self._unset_dump_xml()

    def login(self, auto_refresh=False, force=False):
        """
        Connects to ucsm connected using respective UcsHandle.

        Attributes:
            * auto_refresh (bool): if set to True, it refresh the cookie
              continuously
            * force (bool): if set to True it reconnects even if cookie exists
              and is valid for respective connection.

        Return:
            True on successful connect

        Example:
            handle.login()
            handle.login(auto_refresh=True)
            handle.login(force=True)
            handle.login(auto_refresh=True, force=True)

            where handle is UcsHandle()
        """

        return self._login(auto_refresh, force)

    def logout(self):
        """
        Disconnects from ucsm connected using respective UcsHandle.

        Attributes:
            * None

        Return:
            True on successful disconnect

        Example:
            handle.logout()

            where handle is UcsHandle()
        """

        return self._logout()

    def process_xml_elem(self, elem):
        """
        Processes xml element returned by method factory methods.

        Attributes:
            * elem (xml element object)

        Return:
            mo list or external method object

        Example:
            elem = ucsmethodfactory.config_find_dns_by_class_id(
                                                        cookie=handle.cookie,
                                                        class_id="LsServer",
                                                        in_filter=None)
            dn_objs = handle.process_xml_elem(elem)
        """

        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        if hasattr(response, "out_config"):
            return response.out_config.child
        elif hasattr(response, "out_configs"):
            mo_list = []
            pair_flag = False
            for ch_ in response.out_configs.child:
                if pair_flag or ch_.get_class_id() != "Pair":
                    mo_list.append(ch_)
                elif ch_.get_class_id() == "Pair":
                    mo_list.extend(ch_.child)
                    pair_flag = True
            return mo_list
        elif hasattr(response, "out_dns"):
            return response.out_dns.child
        else:
            return response

    def get_auth_token(self):
        """
            Get ucsm auto token.

        Attributes:
            * None

        Return:
            auth_token (str)

        Example:
            handle.get_auth_token()

            where handle is UcsHandle()
        """

        from ucsmethodfactory import aaa_get_n_compute_auth_token_by_dn

        auth_token = None
        mo = self.query_classid(class_id=NamingId.COMPUTE_BLADE)
        if not mo:
            mo = self.query_classid(class_id=NamingId.COMPUTE_RACK_UNIT)

        if mo:
            elem = aaa_get_n_compute_auth_token_by_dn(
                cookie=self.cookie,
                in_cookie=self.cookie,
                in_dn=mo[0].dn,
                in_number_of=1)
            response = self.post_elem(elem)
            if response.error_code != 0:
                raise UcsException(response.error_code,
                                   response.error_descr)

            # cat = self.AaaGetNComputeAuthTokenByDn(mo[0].Dn, 1, None)
            auth_token = response.out_tokens.split(',')[0]

        return auth_token

    def query_dns(self, *dns):
        """
        Find objects using a comma separated string of distinguished name.

        Attributes:
            * dns (comma separated strings): distinguished names to be
              queried for

        Return:
            Dictionary {dn: object}

        Example:
            obj = handle.lookup_by_dns("fabric/lan/net-100",
                                        "fabric/lan/net-101")
        """

        from ucsbasetype import DnSet, Dn
        from ucsmethodfactory import config_resolve_dns

        if not dns:
            raise ValueError("Provide Comma Separated string of Dns")

        dn_list = [dn.strip() for dn in dns]
        dn_dict = {}
        for dn_ in dn_list:
            dn_dict[dn_] = None

        dn_set = DnSet()
        for dn_ in dn_dict:
            dn_obj = Dn()
            dn_obj.value = dn_
            dn_set.child_add(dn_obj)

        elem = config_resolve_dns(cookie=self.cookie,
                                         in_dns=dn_set)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        for out_mo in response.out_configs.child:
            dn_dict[out_mo.dn] = out_mo

        return dn_dict

    def query_classids(self, *class_ids):
        """
        Find objects using a comma separated string of class ids.

        Attributes:
            * class_ids (comma separated strings): class_id to be queried for

        Return:
            Dictionary {class_id: [list of object]}

        Example:
            obj = handle.lookup_by_dns("OrgOrg",
                                       "LsServer")
        """

        # ToDo - How to handle unknown class_id
        from ucsbasetype import ClassIdSet, ClassId
        from ucsmeta import MO_CLASS_ID

        if not class_ids:
            raise ValueError("Provide Comma Separated string of Class Ids")

        class_id_list = [class_id.strip() for class_id in class_ids]
        class_id_dict = {}
        class_id_set = ClassIdSet()

        for class_id_ in class_id_list:
            class_id_obj = ClassId()

            meta_class_id = ucsgenutils.word_u(class_id_)
            if meta_class_id in MO_CLASS_ID:
                class_id_dict[meta_class_id] = []
                class_id_obj.value = ucsgenutils.word_l(class_id_)
            else:
                class_id_dict[class_id_] = []
                class_id_obj.value = class_id_

            class_id_set.child_add(class_id_obj)

        elem = config_resolve_classes(cookie=self.cookie,
                                             in_ids=class_id_set)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        for out_mo in response.out_configs.child:
            class_id_dict[out_mo._class_id].append(out_mo)

        return class_id_dict

    def query_dn(self, dn, hierarchy=False, need_response=False):
        """
        Find an object using it's distinguished name.

        Attributes:
            * dn (str): distinguished name of the object to be queried for.
            * hierarchy(bool): if set to True will return all the child
                               hierarchical objects.
            * need_response(bool): if set to True will return only response
                                  object.

        Return:
            managedobject or None   by default
            managedobject list      if hierarchy=True
            externalmethod object   if need_response=True

        Example:
            obj = handle.lookup_by_dn("fabric/lan/net-100")
            obj = handle.lookup_by_dn("fabric/lan/net-100", hierarchy=True)
            obj = handle.lookup_by_dn("fabric/lan/net-100", need_response=True)
            obj = handle.lookup_by_dn("fabric/lan/net-100", hierarchy=True,
                                                            need_response=True)
        """

        from ucsbasetype import DnSet, Dn
        from ucsmethodfactory import config_resolve_dns

        if not dn:
            raise ValueError("Provide dn.")

        dn_set = DnSet()
        dn_obj = Dn()
        dn_obj.value = dn
        dn_set.child_add(dn_obj)

        elem = config_resolve_dns(cookie=self.cookie,
                                         in_dns=dn_set,
                                         in_hierarchical=hierarchy)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        if need_response:
            return response

        if hierarchy:
            out_mo_list = ucscoreutils.extract_molist_from_method_response(
                response,
                hierarchy)
            return out_mo_list

        mo = None
        if len(response.out_configs.child) > 0:
            mo = response.out_configs.child[0]
        return mo

    def query_classid(self, class_id=None, filter_str=None, hierarchy=False,
                      need_response=False):
        """
        Find an object using it's class id.

        Attributes:
            * class_id (str): class id of the object to be queried for.
            * filter_str(str): query objects with specific property with
                               specific value or pattern specifying value.

                        (property_name, "property_value, type="filter_type")
                        property_name: Name of the Property
                        property_value: Value of the property (str or regular
                                                               expression)
                        filter_type: eq - equal to
                                     ne - not equal to
                                     ge - greater than or equal to
                                     gt - greater than
                                     le - less than or equal to
                                     lt - less than
                                     re - regular expression

                        logical filter type: not, and, or

                        e.g. '(dn,"org-root/ls-C1_B1", type="eq") or
                        (name, "event", type="re", flag="I")'
            * hierarchy(bool): if set to True will return all the child
                               hierarchical objects.
            * need_response(bool): if set to True will return only response
                                  object.


        Return:
            managedobjectlist or None   by default
            managedobjectlist or None   if hierarchy=True
            methodresponse              if need_response=True

        Example:
            obj = handle.query_classid(class_id="LsServer")
            obj = handle.query_classid(class_id="LsServer", hierarchy=True)
            obj = handle.query_classid(class_id="LsServer", need_response=True)

            filter_str = '(dn,"org-root/ls-C1_B1", type="eq") or
                            (name, "event", type="re", flag="I")'
            obj = handle.query_classid(class_id="LsServer",
                                        filter_str=filter_str)
        """

        # ToDo - How to handle unknown class_id

        from ucsmeta import MO_CLASS_ID
        from ucsfilter import generate_infilter
        from ucsmethodfactory import config_resolve_class

        if not class_id:
            raise ValueError("Provide Parameter class_id")

        if ucsgenutils.word_u(class_id) in MO_CLASS_ID:
            meta_class_id = ucsgenutils.word_l(class_id)
            is_meta_class_id = True
        else:
            meta_class_id = class_id
            is_meta_class_id = False

        if filter_str:
            in_filter = generate_infilter(meta_class_id, filter_str,
                                          is_meta_class_id)
        else:
            in_filter = None

        elem = config_resolve_class(cookie=self.cookie,
                                              class_id=meta_class_id,
                                              in_filter=in_filter,
                                              in_hierarchical=hierarchy)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        if need_response:
            return response

        out_mo_list = ucscoreutils.extract_molist_from_method_response(
                                                                    response,
                                                                    hierarchy)
        return out_mo_list

    def query_children(self, in_mo=None, in_dn=None, class_id=None,
                       hierarchy=False):
        """
        Find all or specific class_id children object of a given managed object
        or a given dn.

        Attributes:
            * in_mo (managed object): query children managed object under this
                                      object.
            * in_dn (dn string): query children managed object for a
                                 given managed object of the respective dn.
            * class_id(str): by default None, if given find only specific
                             children object for a given class_id.
            * hierarchy(bool): if set to True will return all the child
                               hierarchical objects.

        Return:
            managedobjectlist or None   by default
            managedobjectlist or None   if hierarchy=True

        Example:
            mo_list = handle.query_children(in_mo=mo)
            mo_list = handle.query_children(in_mo=mo, class_id="classid")
            mo_list = handle.query_children(in_dn=dn)
            mo_list = handle.query_children(in_dn=dn, class_id="classid")
        """

        from ucsmeta import MO_CLASS_ID
        from ucsmethodfactory import config_resolve_children

        if not in_mo and not in_dn:
            raise ValueError('[Error]: GetChild: Provide in_mo or in_dn.')

        if in_mo:
            parent_dn = in_mo.dn
        elif in_dn:
            parent_dn = in_dn

        if class_id:
            if ucsgenutils.word_u(class_id) in MO_CLASS_ID:
                meta_class_id = ucsgenutils.word_l(class_id)
            else:
                meta_class_id = class_id
        else:
            meta_class_id = class_id

        elem = config_resolve_children(cookie=self.cookie,
                                       class_id=meta_class_id,
                                       in_dn=parent_dn,
                                       in_filter=None,
                                       in_hierarchical=hierarchy)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        out_mo_list = ucscoreutils.extract_molist_from_method_response(
                                                                    response,
                                                                    hierarchy)

        return out_mo_list

    def add_mo(self, mo, modify_present=False):
        """
        Adds an object to the UCSM.

        Attributes:
            * mo (managedobject): ManagedObject to be added.
            * modify_present(bool): if set to True, overwrite the existing
                                    object.

        Return:
            None

        Example:
            obj = handle.add_mo(mo)
            handle.commit()
        """

        if modify_present in ucsgenutils.AFFIRMATIVE_LIST:
            mo.status = "created,modified"
        else:
            mo.status = "created"

        self.__to_commit[mo.dn] = mo

    def set_mo(self, mo):
        """
        Modifies configuration of an object.

        Attributes:
            * mo (managedobject): ManagedObject with modified properties.

        Return:
            None

        Example:
            obj = handle.set_mo(mo)
            handle.commit()
        """

        mo.status = "modified"
        self.__to_commit[mo.dn] = mo

    def remove_mo(self, mo):
        """
        Removes object from UCSM.

        Attributes:
            * mo (managedobject): ManagedObject to be removed.

        Return:
            None

        Example:
            obj = handle.remove_mo(mo)
            handle.commit()
        """

        mo.status = "deleted"
        if mo.parent_mo:
            mo.parent_mo.child_remove(mo)

        self.__to_commit[mo.dn] = mo

    def commit(self):
        """
        Sends the object to UCSM.
        Add, modify or remove using add_mo(), set_mo() and remove_mo()
        respectively.

        Return:
            None

        Example:
            handle.commit()
        """

        from ucsbasetype import ConfigMap, Dn, DnSet, Pair
        from ucsmethodfactory import config_resolve_dns
        from ucsmethodfactory import config_conf_mos

        refresh_dict = {}
        mo_dict = self.__to_commit
        if not mo_dict:
            log.debug("No Mo to be Committed")
            return None

        config_map = ConfigMap()
        for mo_dn in mo_dict:
            mo = mo_dict[mo_dn]
            child_list = mo.child
            while len(child_list) > 0:
                current_child_list = child_list
                child_list = []
                for child_mo in current_child_list:
                    if child_mo.is_dirty():
                        refresh_dict[child_mo.dn] = child_mo
                    child_list.extend(child_mo.child)

            pair = Pair()
            pair.key = mo_dn
            pair.child_add(mo_dict[mo_dn])
            config_map.child_add(pair)

        elem = config_conf_mos(self.cookie, config_map,
                                         False)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise UcsException(response.error_code, response.error_descr)

        for pair_ in response.out_configs.child:
            for out_mo in pair_.child:
                out_mo.sync_mo(mo_dict[out_mo.dn])

        if refresh_dict:
            dn_set = DnSet()
            for dn_ in refresh_dict:
                dn_obj = Dn()
                dn_obj.value = dn_
                dn_set.child_add(dn_obj)

            elem = config_resolve_dns(cookie=self.cookie,
                                                in_dns=dn_set)
            response = self.post_elem(elem)
            if response.error_code != 0:
                raise UcsException(response.error_code,
                                      response.error_descr)

            for out_mo in response.out_configs.child:
                out_mo.sync_mo(refresh_dict[out_mo.dn])

        self.__to_commit = {}

    def commit_buffer_discard(self):
        """
        clears the commit buffer

        Return:
            None

        Example:
            handle.commit_buffer_discard()
        """

        self.__to_commit = {}
