Table of Contents
=================

1.  `Overview <#overview>`__
2.  `Management Information Model <#management-information-model>`__

    1. `Managed Objects <#managed-objects>`__
    2. `References To Managed
       Objects <#references-to-managed-objects>`__
    3. `Properties Of Managed
       Objects <#properties-of-managed-objects>`__
    4. `Methods <#methods>`__

3.  `Installation <#installation>`__

    1. `Pre-install Checklist <#pre-install-checklist>`__
    2. `Installation Steps <#installation-steps>`__

4.  `Uninstallation <#uninstallation>`__

    1. `Uninstallation Steps <#uninstallation-steps>`__

5.  `Getting Started <#getting-started>`__

    1. `Connecting Disconnecting <#connecting-disconnecting>`__
    2. `Base APIs <#basic-apis>`__
    3. `Creating Objects <#creating-objects>`__
    4. `Querying Objects <#querying-objects>`__
    5. `Querying Objects With
       Filters <#querying-objects-with-filters>`__
    6. `Modifying Objects <#modifying-objects>`__
    7. `Deleting Objects <#deleting-objects>`__
    8. `Transaction <#transaction>`__

6.  `Convert To Ucs Python <#convert-to-ucs-python>`__
7.  `Retrieving Meta Information <#retrieving-meta-information>`__
8.  `Watch Ucs Events <#watch-ucs-events>`__

    1. `Wait Until Condition <#wait-until-condition>`__

9.  `Backup And Import <#backup-and-import>`__

    1. `Backup Ucs <#backup-ucs>`__
    2. `Import Ucs <#import-ucs>`__

10. `Start GUI Session <#start-gui-session>`__
11. `Start KVM Session <#start-kvm-session>`__
12. `Technical Support <#technical-support>`__
13. `Advanced Features <#advanced-features>`__

    1. `Compare And Sync UCS <#compare-and-sync-ucs>`__
    2. `Multiple Parallel
       Transactions <#multiple-parallel-transactions>`__
    3. `Threading Mode <#threading-mode>`__

Overview
--------

Cisco UCS Python SDK is a python module which helps automate all aspects
of Cisco UCS management including server, network, storage and
hypervisor management.

Bulk of the Cisco UCS Python SDK work on the UCS Manager’s Management
Information Tree (MIT), performing create, modify or delete actions on
the Managed Objects (MO) in the tree. The next chapter provides an
overview of the Cisco UCS Management Information Model (MIM).

One of the easiest ways to learn UCS configuration through UCS Python
SDK is to automatically generate python script, for configuration
actions performed with the UCSM GUI, using API described in `Convert To
Ucs Python <#convert-to-ucs-python>`__.

Management Information Model
----------------------------

All the physical and logical components that comprise Cisco UCS are
represented in a hierarchical Management Information Model, referred to
as the Management Information Tree (MIT). Each node in the tree
represents a Managed Object (MO), uniquely identified by its
Distinguished Name. (DN)

The figure below illustrates a sample (partial) MIT for three chassis.

::

    Tree (topRoot)              Distinguished Name
    |— sys                      sys
    |— chassis-1                    sys/chassis-1
    |— chassis-2                    sys/chassis-2
    |— chassis-3                    sys/chassis-3
        |— blade-1              sys/chassis-3/blade-1
        |       |— adaptor-1        sys/chassis-3/blade-1/adaptor-1
        |— blade-2              sys/chassis-3/blade-2
                |— adaptor-1        sys/chassis-3/blade-2/adaptor-1
                |— adaptor-2        sys/chassis-3/blade-2/adaptor-2

Managed Objects
~~~~~~~~~~~~~~~

Managed Objects (MO) are abstractions of Cisco UCS resources, such as
fabric interconnects, chassis, blades, and rack-mounted servers. Managed
Objects represent any physical or logical entity that is configured /
managed in the Cisco UCS MIT. For example, physical entities such as
Servers, Chassis, I/O cards, Processors and logical entities such as
Resource pools, User roles, Service profiles, and Policies are
represented as Managed Objects.

Every Managed Object is uniquely identified in the tree with its
Distinguished Name (Dn) and can be uniquely identified within the
context of its parent with its Relative Name (Rn). The Dn identifies the
place of the MO in the MIT. A Dn is a concatenation of all the relative
names starting from the root to the MO itself. Essentially, Dn =
[Rn]/[Rn]/[Rn]/…/[Rn].

In the example below, Dn provides a fully qualified name for adaptor-1
in the model.

::

    <dn = “sys/chassis-5/blade-2/adaptor-1” />

The above written Dn is composed of the following Rn:

::

    topSystem MO: rn="sys"
    equipmentChassis MO: rn="chassis-[id]"
    computeBlade MO: rn ="blade-[slotId]"
    adaptorUnit MO: rn="adaptor-[id]"

A Relative Name (Rn) may have the value of one or more of the MO’s
properties embedded in it. This allows in differentiating multiple MOs
of the same type within the context of the parent. Any properties that
form part of the Rn as described earlier are referred to as Naming
properties.

For instance, multiple blade MOs reside under a chassis MO. The blade MO
contains the blade identifier as part of its Rn (blade-[Id]), thereby
uniquely identifying each blade MO in the context of a chassis.

References To Managed Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The contents of the Managed Objects are referred to during the operation
of UCS. Some of the MOs are referred to implicitly (PreLoginBanner
during login) or as part of deployment of another MO (The Service
Profile MO may refer to a template or a VNIC refers to a number of VLAN
MOs).

A singleton MO type is found utmost once in the entire MIT and is
typically referred to implicitly.

Non-Singleton MO type may be instantiated one or more times in the MIT.
In many cases, when an MO refers to another, the reference is made by
name. Depending on the type of the referenced MO, the resolution may be
hierarchical. For instance, a service profile template is defined under
an Org. Since an org may contain sub-orgs, a sub org may have a service
profile template defined with the same name. Now, when a service profile
instance refers to a service profile template (by name), the name is
looked up hierarchically from the org of the service profile instance up
until the root org. The first match is used. If no match is found, then
the name “default” is looked up in the similar way and the first match
is used.

Properties of Managed Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties of Managed Objects can be classified as Configuration or
Operational.

Configuration properties may be classified as:

-  Naming properties: Form part of the Rn. **Needs** to be specified
   only during MO creation and cannot be modified later.
-  Create-Only properties: **May** be specified only during MO creation
   and cannot be modified later. If the property is not specified, a
   default value is assumed.
-  Read / Write properties: **May** be specified during MO creation and
   can also be modified subsequently.

Operational properties indicate the current status of the MO / system
and are hence read-only.

Methods
~~~~~~~

Methods are Cisco UCS XML APIs, used to manage and monitor the system.
There are methods supported for:

-  Authentication

   -  AaaLogin
   -  AaaRefresh
   -  AaaLogout

-  Configuration

   -  ConfigConfMo(s)
   -  LsClone
   -  LsInstantiate\*
   -  FaultAckFaults

-  Query

   -  ConfigResolveDn(s)
   -  ConfigResolveClass(es)
   -  ConfigResolveChildren

-  Event Monitor

   -  EventSubscribe

The class query methods (ConfigResolveClass(es), ConfigResolveChildren)
allow a filter to be specified so that a specific set of MOs are matched
and returned by the method.

The supported filters are:

-  allbits – Match if all specified values are present in a multi-valued
   property
-  anybit – Match if any of the specified values are present in a
   multi-valued property
-  bw – Match if the property’s value lies between the two values
   specified
-  eq – Match if property’s value is the same as the specified value
-  ge – Match if property’s value is greater than or equal to the
   specified value
-  gt - Match if property’s value is greater than the specified value
-  le – Match if property’s value is lesser than or equal to the
   specified value
-  lt – Match if property’s value is lesser than the specified value
-  ne – Match if property’s value is not equal to the specified value
-  wcard – Match if property’s value matches the pattern specified

Installation
------------

Pre-install Checklist
~~~~~~~~~~~~~~~~~~~~~

Ensure the following are available

::

    python >= 2.7
    pip

Installation Steps
~~~~~~~~~~~~~~~~~~

-  Installing the last released version of the SDK from pypi

::

    pip install ucsmsdk

-  Installing the latest developer version from github

::

    git clone https://github.com/CiscoUcs/ucsmsdk/
    cd ucsmsdk
    sudo make install

Uninstallation
--------------

Uninstallation Steps
~~~~~~~~~~~~~~~~~~~~

Irrespective of the method that was used to install the SDK, it can be
uninstalled using the below command,

::

    pip uninstall ucsmsdk

Getting Started
---------------

Connecting Disconnecting
~~~~~~~~~~~~~~~~~~~~~~~~

::

    from ucsmsdk.ucshandle import UcsHandle

    # Create a connection handle
    handle = UcsHandle("192.168.1.1", "admin", "password")

    # Login to the server
    handle.login()

    # Logout from the server
    handle.logout()

Refer `UcsHandle API
Reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#module-ucsmsdk.ucshandle>`__
for detailed parameter sets to ``UcsHandle``

Base APIs
~~~~~~~~~

The SDK provides APIs to enable CRUD operations.

-  **C**\ reate an object - ``add_mo``
-  **R**\ etrieve an object -
   ``query_dn``,\ ``query_classid``,\ ``query_dns``,\ ``query_classids``
-  **U**\ pdate an object - ``set_mo``
-  **D**\ elete an object - ``delete_mo``

The above APIs can be bunched together in a transaction (All or None).
``commit_mo`` commits the changes made using the above APIs.

All these methods are invoked on a ``UcsHandle`` instance. We refer it
by ``handle`` in all the examples here-after. Refer to the `Connecting
Disconnecting <#connecting-disconnecting>`__ to create a new handle.

Creating Objects
~~~~~~~~~~~~~~~~

Creating managed objects is done via ``add_mo`` API.

Example:

The below example creates a new Service Profile(\ ``LsServer``) Object
under the parent ``org-root``

::

    from ucsmsdk.mometa.ls.LsServer import LsServer

    sp = LsServer(parent_mo_or_dn="org-root", name="sp_demo")
    handle.add_mo(sp)

**note**: the changes will only be sent to server when
``handle.commit()`` is called.

`Add Mo API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.add_mo>`__

Querying Objects
~~~~~~~~~~~~~~~~

-  Querying Objects via Distinguished Name (DN)

   ::

       object = handle.query_dn("org-root/ls-sp_demo")

-  Querying Multiple Objects via Multiple Distinguished Names (DN)

   The returned object is a dictionary in ``{dn:object}`` format

   ::

       object_dict = handle.query_dn("org-root/ls-sp_demo1", "org-root")

-  Querying Objects via class Id

   The below returns all objects of type ``orgOrg``

   ::

       object_array = handle.query_classid("orgOrg")

-  Querying Objects via multiple class Ids

   The below returns all objects of type ``orgOrg`` and ``fabricVlan``.
   The output is a dictionary of format ``{classId: [objects]}``

   ::

       object_dict = handle.query_classid("orgOrg", "fabricVlan")

`Query DN API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.query_dn>`__

`Query DNs API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.query_dns>`__

`Query Class Id API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.query_classid>`__

`Query Class Ids API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.query_classids>`__

Querying Objects With Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filter is passed as string parameter to
``query_dn``,\ ``query_dns``,\ ``query_classid``,\ ``query_classids``
methods

-  Basic usage:

   A basic filter string is of ``(prop_name, prop_value)`` format,

   ::

       filter_str = '(name, "demo_1")'
       sp = handle.query_classid(class_id="LsServer", filter_str=filter_str)

-  Specific usage:

   To have more control on the filter behaviour use the extended filter
   format, ``(prop_name, prop_value, filter_type)``

   **filter\_type**:

   -  ``re``: Default, regex match.
   -  ``eq``: equal, exact match.
   -  ``ne``: not equal
   -  ``ge``: greater than and equal to
   -  ``gt``: greater than
   -  ``le``: less than and equal to
   -  ``lt``: less than

   An example of an exact match,

   ::

       filter_str = '(name, "demo_1", type="eq")'
       sp = handle.query_classid(class_id="LsServer", filter_str=filter_str)

-  Complex filters - combination of multiple conditions:

   The below checks for ``(name == "demo")`` or
   ``(name == *demo_1* and name == [0-9]_1)``

   ::

       filter_str = '''(name, "demo", type="eq") or ((name, "demo_1") and
                                                   (name, "[0-9]_1"))'''
       sp = handle.query_classid(class_id="LsServer", filter_str=filter_str)

   **note**: ``'''`` here is used as a multiline string

Modifying Objects
~~~~~~~~~~~~~~~~~

``set_mo`` is used for updating an existing object

::

    # Query for an existing Mo
    sp = handle.query_dn("org-root/ls-sp_demo")

    # Update description of the service profile
    sp.descr = "demo_descr"

    # Add it to the on-going transaction
    handle.set_mo(sp)

**note**: The changes will not be sent to the server until a
``commit()`` is invoked.

`Set Mo API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.set_mo>`__

Deleting Objects
~~~~~~~~~~~~~~~~

``remove_mo`` is used for removing an object

::

    # Query for an existing Mo
    sp = handle.query_dn("org-root/ls-sp_demo")

    # Remove the object
    handle.remove_mo(sp)

**note**: The changes will not be sent to the server until a
``commit()`` is invoked.

`Remove Mo API
reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.html#ucsmsdk.ucshandle.UcsHandle.remove_mo>`__

Transaction
~~~~~~~~~~~

API operations are batched together by default until a ``commit()`` is
invoked.

In the below code, the objects are created only when ``commit`` is
invoked. If there is a failure in one of the steps, then no changes are
committed to the server.

::

    from ucsmsdk.mometa.ls.LsServer import LsServer

    sp1 = LsServer(parent_mo_or_dn="org-root", name="sp_demo1")
    handle.add_mo(sp1)

    sp2 = LsServer(parent_mo_or_dn="org-root", name="sp_demo2")
    handle.add_mo(sp2)

    # commit the changes to server
    handle.commit()

Convert To Ucs Python
---------------------

Wouldn't it be cool if you did not have to know the SDK much to be able
to automate operations based off it?

Welcome the ``convert_to_ucs_python`` API.

**Assumption**:

-  User knows to do an operation via the JAVA based UCSM GUI
-  UCSM UI and ``convert_to_ucs_python`` should be launched on the same
   client machine.

**Basic Idea**:

-  launch the JAVA based UCSM UI
-  launch the python shell and invoke ``convert_to_ucs_python``
-  perform the desired operation on the UI
-  ``convert_to_ucs_python`` monitors the operation and generates
   equivalent python script for the same.

**How it works**:

-  UCSM GUI logs all the activities that are performed via it, and the
   python shell monitors that log to generate the equivalent python
   script. Since the logging is local to the machine where the UI is
   running, ``convert_to_ucs_python`` also must run on the same machine.

**Sample Usage**:

Step 1 - Launch the UCSM GUI.

::

    from ucsmsdk.utils.ucsguilaunch import ucs_gui_launch
    from ucsmsdk.ucshandle import UcsHandle

    # Login to the server
    handle = UcsHandle(<ip>, <username>, <password>)
    handle.login()

    # launch the UCSM GUI
    ucs_gui_launch(handle)

Step 2 - Run ``convert_to_ucs_python``

The CLI will go into a listen mode until ``Ctrl+C`` is pressed again.
Until then it prints equivalent script for operations done on the UI.

-  Print the equivalent script to console

::

    from ucsmsdk.utils.converttopython import convert_to_ucs_python

    convert_to_ucs_python()

-  Print the equivalent script to console, also print the XMLs that the
   UI sends out

::

    from ucsmsdk.utils.converttopython import convert_to_ucs_python

    convert_to_ucs_python(dump_xml=True)

-  Output the script to a file

::

    from ucsmsdk.utils.converttopython import convert_to_ucs_python

    file_path = r”/home/user/pythoncode.py”

    convert_to_ucs_python(dump_to_file=True, dump_file_path=file_path)

-  XML to python

::

    xml_str=’‘’<configConfRename
                    dn=”org-root/ls-ra1”
                    inNewName=”ra2”
                    inHierarchical=”false”>
                    </configConfRename>’‘’

    convert_to_ucs_python(xml=True, request=xml_str)

API documentation: \ ``convert_to_ucs_python``\

**note**:

The path of UCSM UI logs differs based on the OS and so sometimes the
``convert_to_ucs_python`` API may not be able to autodetect the path.
The following workaround can be applied in such cases,

-  Manually find the path to UCSM UI logs

::


    $ sudo find / -name '.ucsm'
    ./Library/Application Support/Oracle/Java/Deployment/log/.ucsm
    $

-  Run ``convert_to_ucs_python`` by specifying the ``path``

::

    from ucsmsdk.utils.converttopython import convert_to_ucs_python

    convert_to_ucs_python(gui_log=True, path=<path that was found above>)

Retrieving Meta Information
---------------------------

``get_meta_info`` is useful for getting information about a Managed
object.

::

    from ucsmsdk.ucscoreutils import get_meta_info

    class_meta = get_meta_info("FabricVlan")
    print class_meta

The below sample output starts with a tree view of where FabricVlan
fits, its parents and childrens, followed by MO information. It then
shows information about properties of the MO.

-  Mo Property information:

   -  ``xml_attribute`` - the name of the property as expected by the
      server.
   -  ``field_type`` - type of the field
   -  ``min_version`` - Ucs server release in which the property was
      first introduced
   -  ``access`` - defines if a property is
      interal/user-readable/user-writable
   -  property restrictions:

      -  ``min_length`` - minimum length for string property type
      -  ``max_length`` - maximum length for string property type
      -  ``pattern`` - allowed patterns, regexs
      -  ``value_set`` - set of allowed values for this property
      -  ``range_val`` - range for int/uint values

sample output: (truncated)

::

    [FabricEthEstc]
    [FabricEthEstcCloud]
    [FabricEthLan]
    [FabricLanCloud]
      |-FabricVlan
         |-FabricEthMonFiltEp
         |-FabricEthMonSrcEp
         |-FabricEthVlanPc
         |  |-FaultInst
         |-FabricEthVlanPortEp
         |  |-FaultInst
         |-FabricPoolableVlan
         |-FabricSwSubGroup
         |  |-FabricEthVlanPortEp
         |  |  |-FaultInst
         |  |-FabricFcoeVsanPortEp
         |     |-FaultInst
         |-FaultInst

    ClassId                         FabricVlan
    -------                         ----------
    xml_attribute                   :fabricVlan
    rn                              :net-[name]
    min_version                     :1.0(1e)
    access                          :InputOutput
    access_privilege                :['admin', 'ext-lan-config', 'ext-lan-policy']
    parents                         :[u'fabricEthEstc', u'fabricEthEstcCloud', u'fabricEthLan', u'fabricLanCloud']
    children                        :[u'fabricEthMonFiltEp', u'fabricEthMonSrcEp', u'fabricEthVlanPc', u'fabricEthVlanPortEp', u'fabricPoolableVlan', u'fabricSwSubGroup', u'faultInst']

    Property                        assoc_primary_vlan_state
    --------                        ------------------------
    xml_attribute                   :assocPrimaryVlanState
    field_type                      :string
    min_version                     :2.2(2c)
    access                          :READ_ONLY
    min_length                      :None
    max_length                      :None
    pattern                         :None
    value_set                       :['does-not-exists', 'is-empty', 'is-in-error-state', 'is-not-primary-type', 'ok']
    range_val                       :[]

    Property                        assoc_primary_vlan_switch_id
    --------                        ----------------------------
    xml_attribute                   :assocPrimaryVlanSwitchId
    field_type                      :string
    min_version                     :2.2(2c)
    access                          :READ_ONLY
    min_length                      :None
    max_length                      :None
    pattern                         :None
    value_set                       :['A', 'B', 'NONE']
    range_val                       :[]

Watch Ucs Events
----------------

Wait Until Condition
~~~~~~~~~~~~~~~~~~~~

``wait_for_event`` is used to wait until a specific condition.

It works by monitoring the Ucs Event Channel or by periodically polling
the server. Polling mode is used when ``poll_sec`` argument is specified.
Specifying a timeout is highly recommended.

Arguments:

-  mo: object that is monitored
-  prop: prop to check
-  value: success value
-  cb: done callback
-  timeout: (Optional) timeout in seconds
-  poll_sec: (Optional) polling interval in seconds when using poll mode

::

    def done_callback(mo_change_event):
        print mo_change_event.mo


    sp_mo = handle.query_dn("org-root/ls-sp_demo")

    # call done_callback when (sp_mo.descr == "demo")
    handle.wait_for_event(sp_mo, "descr", "demo", done_callback)


Backup And Import
-----------------

Backup Ucs
~~~~~~~~~~

``backup_ucs`` is used to take backup of a Ucs server

Type of backups:

-  ``fullstate``
-  ``config-logical``
-  ``config-system``
-  ``config-all``

::

    from ucsmsdk.utils.ucsbackup import backup_ucs

    backup_dir = “/home/user/backup”
    backup_filename = “config_backup.xml”

    backup_ucs(handle,
                 backup_type=”config-logical”,
                 file_dir= backup_dir,
                 file_name= backup_filename)

`Backup Ucs API
Reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.utils.html#ucsmsdk.utils.ucsbackup.backup_ucs>`__

Import Ucs
~~~~~~~~~~

``import_ucs_backup`` is used to import an existing backup to a Ucs
server

::

    from ucsmsdk.utils.ucsbackup import import_ucs_backup

    import_dir = “/home/user/backup”
    import_filename = “config_backup.xml”

    import_ucs_backup(handle,
                         file_dir=import_dir,
                         file_name=import_filename)

`Import Ucs API
Reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.utils.html#ucsmsdk.utils.ucsbackup.import_ucs_backup>`__

Start GUI Session
-----------------

``ucs_gui_launch`` is used to launch UCSM JAVA GUI.

This method assumes that the required JAVA installation for UCSM UI is
already present.

::

    from ucsmsdk.utils.ucsguilaunch import ucs_gui_launch

    ucs_gui_launch(handle)

`Start UCS GUI API
Reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.utils.html#ucsmsdk.utils.ucsguilaunch.ucs_gui_launch>`__

**note**: This method is specific to launching UCSM JAVA GUI. It does
not work for UCSM HTML UI

Start KVM Session
-----------------

``ucs_kvm_launch`` is used to launch KVM for a service profile or a
server(blade/rack)

-  Launch KVM for a specified service profile MO

::

    from ucsmsdk.utils.ucskvmlaunch import ucs_kvm_launch

    # sp_mo is of type LsServer
    ucs_kvm_launch(handle, service_profile=sp_mo)

-  Launch KVM for a specified Blade server

::

    from ucsmsdk.utils.ucskvmlaunch import ucs_kvm_launch

    # blade_mo is of type ComputeBlade
    ucs_kvm_launch(handle, blade=blade_mo)

-  launch KVM for a specified Rack server

::

    from ucsmsdk.utils.ucskvmlaunch import ucs_kvm_launch

    # rack_mo is of type ComputeRackUnit
    ucs_kvm_launch(handle, rack_unit=rack_mo)

`Start KVM Session API
Reference <https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk.utils.html#ucsmsdk.utils.ucskvmlaunch.ucs_kvm_launch>`__

Technical Support
-----------------

``get_tech_support`` facilitates technical support for UCSM and related
components. ``option`` parameter defines the type of technical support that is
desired. ``**kwargs`` are ``key1=val1, key2=val2`` type named arguments that
need to be specified depending on the component for which technical support is
being trigerred.

For example, if the user wants to trigger technical support for
``option=chassis``, then he/she will also need to pass
``chassis_id=1, cimc_id=1`` or ``chassis_id=1, iom_id=1``.

The below examples show the corresponding arguments that apply to the
component for which tech support is being taken. Please note that these
parameters should only be specified towards the end and not before the existing
named paramters.

- Create Tech Support for UCSM

::

    from ucsmsdk.utils.ucstechsupport import get_tech_support
    get_tech_support(handle,
                     option="ucsm",
                     file_dir='.',
                     file_name="ucsm.tar",
                     timeout=1800)


- Create Tech Support for UCSM-MGMT

::

    from ucsmsdk.utils.ucstechsupport import get_tech_support
    get_tech_support(handle,
                     option="ucsm-mgmt",
                     file_dir='.',
                     file_name="ucsm.tar",
                     timeout=1800)

- Create Tech Support for Chassis-CIMC

::

    from ucsmsdk.utils.ucstechsupport import get_tech_support
    get_tech_support(handle,
                     option="chassis",
                     file_dir='.',
                     file_name="cimc.tar",
                     timeout=1800,
                     chassis_id=1,
                     cimc_id=1,
                     adapter_id="all"
                     )

- Create Tech Support for Chassis-IOM

::

    from ucsmsdk.utils.ucstechsupport import get_tech_support
    get_tech_support(handle,
                     option="chassis",
                     file_dir='.',
                     file_name="cimc.tar",
                     timeout=1800,
                     chassis_id=1,
                     iom_id=1,
                     )

- Create Tech Support for Rackserver

::

    from ucsmsdk.utils.ucstechsupport import get_tech_support
    get_tech_support(handle,
                     option="rack-server",
                     file_dir='.',
                     file_name="cimc.tar",
                     timeout=1800,
                     rack_server_id=1,
                     rack_adapter_id="all"
                     )

- Create Tech Support for Fabric Extender

::

    from ucsmsdk.utils.ucstechsupport import get_tech_support
    get_tech_support(handle,
                     option="fabric-extender",
                     file_dir='.',
                     file_name="fex.tar",
                     timeout=1800,
                     fex_id=1
                     )



Advanced Features
-----------------

Compare And Sync UCS
~~~~~~~~~~~~~~~~~~~~

``compare_ucs_mo`` is used to compare objects with same ``dn`` across
different Ucs Domains.

Compare objects with same DN on different domains

::

    dn_to_compare = ”org-root/ls-sp”
    ref_mo = [ref_handle.query_dn(dn=dn_to_compare)]
    diff_mo = [diff_handle.query_dn(dn=dn_to_compare)]

    difference = compare_ucs_mo(ref_mo, diff_mo)

``sync_ucs_mo`` is used to sync changes that are found using
``compare_ucs_mo``

::

    # difference parameter is the output of compare_ucs_mo
    sync_ucs_mo(ref_handle,
                  difference=difference,
                  delete_not_present=True)

Multiple Parallel Transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional ``tag`` parameter in ``add_mo``, ``set_mo``, ``remove_mo``,
``commit`` provides a scope to transaction.

This enables multiple parallel transactions,

::

    handle.add_mo(mo1, tag="trans_1")
    handle.add_mo(mo2, tag="trans_2")
    handle.add_mo(mo3, tag="trans_1")
    handle.remove_mo(mo4, tag="trans_2")

    # Commit transaction #2
    handle.commit(tag="trans_2")

    handle.add_mo(mo5, tag="trans_1")

    # Commit transaction #1
    handle.commit(tag="trans_1")

Threading Mode
~~~~~~~~~~~~~~

This mode is useful, when the application that uses the SDK is threaded
and it intends to use the SDK using its multiple threads.

-  Enable threaded mode

   ::

       handle.set_mode_threading()

-  Disable threaded mode

   ::

       handle.unset_mode_threading()

When threading mode is enabled the transaction context isolation is
automatically provided on a thread level (even when the ``tag``
parameter is not explicitly specified). Thread names are automatically
used as ``tag`` parameter internally.
