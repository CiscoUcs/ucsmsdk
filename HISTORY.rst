.. :changelog:

History
-------

0.9.22 (2025-05-15)
---------------------
* Support for UCSM release 4.3(6a)

0.9.21 (2024-11-05)
---------------------
* Support for UCSM release 4.3(5a)

0.9.20 (2024-09-20)
---------------------
* Fixes for encoding failure during firmware upload 

0.9.19 (2024-08-28)
---------------------
* Support for UCSM release 4.3(4b)

0.9.18 (2024-06-13)
---------------------
* Support for UCSM release 4.3(4a)

0.9.17 (2024-04-19)
---------------------
* Support for UCSM release 4.3(3a)

0.9.16 (2023-10-12)
---------------------
* Fixes the issue where acknowledging a fault was not working via  ucsmsdk

0.9.15 (2023-08-29)
---------------------
* Support for UCSM release 4.3(2b)

0.9.14 (2023-01-13)
---------------------
* Support for UCSM release 4.2(3b)

0.9.13 (2022-07-21)
---------------------
* Support for UCSM release 4.2(2a)

0.9.12 (2021-08-30)
---------------------
* Fixes for python 3.9 compatibility
* Fixes issue in earlier release

0.9.11 (2021-08-25)
---------------------
* Support for UCSM release 4.2(1a)


0.9.10 (2020-04-23)
---------------------
* Support for UCSM release 4.1(1a), 4.1(1b), 4.1(1c)

0.9.9 (2019-12-20)
---------------------
* Support for UCSM release 4.0(4a)


0.9.8 (2019-01-22)
---------------------
* Support for UCSM release 4.0(2a)


0.9.6 (2018-12-11)
---------------------
* Support for UCSM release 4.0(1b)


0.9.5 (2018-10-10)
---------------------
* Updated requirements to include setuptools


0.9.4 (2018-08-13)
---------------------
* Fixes for python 3 compatibility


0.9.3.2 (2018-04-25)
---------------------
* Support for UCSM release 3.2(3a)
* Support for accepting array arguments in query_classids, query_dns
* Support for setting response timeout for the UCSM operations (query/config)
* Handling `auto_refresh` flag in unfreeze
* Fixing issue with None value check of property by removing None check from validation of property/check_prop_match
* Fixing issue where error happens with commit when threading is enabled and commit buffer is empty
* Fixing issue where ssl with "Only TLS 1.2" does not work

0.9.3.1 (2017-01-25)
---------------------

* Removed `jsonpickle` dependency

0.9.3.0 (2017-01-25)
---------------------

* Support for estimating impact of a transaction - `handle.estimate_impact`
* Support for TLS 1.1, 1.2 Newer UCSM releases support TLS1.2. HTTPS connection
  to the servers with newer releases might fail in absence of TLS1.1/1.2
  support.
* Added command line script to make running `convert_to_ucs_python` easier.
  bin/watch_ucs.py in the github repo.
* Special characters like <,>,& in XML values are deemed invalid and cause
  failure in parsing XML. Added a recovery logic if these exist in the XML
  value fields.
* Support for serialization, deserialization of UcsHandle
* Support for UCSM inventory via `get_inventory` API

0.9.2.0 (2016-09-21)
---------------------

* Support for UCSM 3.1(2b)
* Adds Support for Generating python APIs from a Ucs backup xml -
  `convert_from_backup`
* Adds Infra to facilitate and notify users of API deprecation
* Allows the ucsmsdk/apis layer APIs to pass in None values to indicate that no
  change is rquested to those specific params
* Adds a method to check if the handle.cookie is still valid
* Fix in eventhandlers, where some events were not getting processed
* Fix in eventhandlers, where timeout was not getting triggered until new
  events
* Fix in get_ucs_tech_support, where techsupport for rack server was failing
* Fix in logout, where a Ctrl+C was causing stale connections on the server
* Deprecated `get_ucs_tech_support` in favour of `get_tech_support`. The newer
  API simplifies the API

0.9.1.1 (2016-07-12)
---------------------

* Support for UCSM 2.2.7
* Simplified event handlers to a single `wait_for_event` method. `UcsEventHandler` internals are hidden from user.
* Support for showing progress for upload/download operations
* Support for multi-threading in SDK. An application can run multiple threads that can use SDK methods in parallel.
* Support for multiple parallel transactions via the `tag` parameter in `add_mo`, `set_mo`, `remove_mo`, `commit_mo`
* Fix for `convert_to_ucs_python` exception in some scenarios
* Fix for `convert_to_ucs_python` not displaying python script for Java6u45
* Fix for event handlers not trigerring for some events
* Added more unit and system tests
* Better Documentation

0.9.1.0 (2016-05-25)
---------------------

* Support for UCSM 3.1.1
* Support for Python 3.x
* Support for Comparing and Syncing Objects across Ucs Domains - `compare_ucs_mo` `sync_ucs_mo`
* Support for `filter_str` in `query_children` method
* Support to drill down into Managed Object Meta and Property Meta details - `get_meta_info`
* Support to monitor **any/all** change(s) in a ManagedObject with `UcsEventHandler`
* Fix for Unable to make unsecured connection when redirection was enabled on the server
* Fix for issues with the usage of force parameter in `Login` method
* Fix for `not` filter not generating filter request
* Fix for TechSupport not getting removed from server even when `remove_from_ucs=True`
* Fix for convert_to_ucs_python not redirecting output to a file
* Fix for convert_to_ucs_python not working correctly when `gui_log=True`
* More PEP8 compliance related fixes

0.9.0.0 (2015-01-11)
---------------------

* Python SDK for UCS server management and related automation
* Supports every Managed Object exposed by Ucs
* APIs for CRUD operations simplified
* Support for server side filters made simpler
* Support for eventhandlers
* Runtime memory usage is reduced
* Nosetests for unit testing
* Samples directory for more real world use cases
* Integrating the sphinx framework for documentation
* PEP8 Compliance
