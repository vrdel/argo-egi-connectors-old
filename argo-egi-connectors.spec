Name: argo-egi-connectors
Version: 1.7.4
Release: 1%{?dist}
Group: EGI/SA4
License: ASL 2.0
Summary: Components generate input for ARGO Compute Engine
Url: http://argoeu.github.io/guides/sync/
Vendor: SRCE <dvrcic@srce.hr>, SRCE <kzailac@srce.hr>

Obsoletes: ar-sync
Prefix: %{_prefix}
Requires: argo-ams-library
Requires: avro
Requires: python-requests
Requires: python2-ndg_httpsclient
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Installs the components for syncing ARGO Compute Engine
with GOCDB, VAPOR and POEM definitions per day.

%prep
%setup -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
install --directory %{buildroot}/%{_sharedstatedir}/argo-connectors/
install --directory %{buildroot}/%{_localstatedir}/log/argo-connectors/
install --directory %{buildroot}/%{_libexecdir}/argo-egi-connectors/

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%config(noreplace) /etc/argo-egi-connectors/*
%attr(0755,root,root) %dir %{_libexecdir}/argo-egi-connectors/
%attr(0755,root,root) %{_libexecdir}/argo-egi-connectors/*.py*

%attr(0755,root,root) %dir %{_sharedstatedir}/argo-connectors/
%attr(0755,root,root) %dir %{_localstatedir}/log/argo-connectors/

%changelog
* Mon Mar 30 2020 Daniel Vrcic <dvrcic@srce.hr> - 1.7.4-1%{dist}
- ARGO-2247 Pass URL from EOSC topology
- ARGO-2225 Support for creating empty weights and downtimes data
- ARGO-2221 Metric profile namespace optional 
- ARGO-2210 Introduce topology connector for EOSC-PORTAL
- ARGO-2209 Pass PRIMARY_KEY of GOCDB service endpoint as a unique service endpoint identifier 
* Fri Nov 8 2019 Daniel Vrcic <dvrcic@srce.hr> - 1.7.3-1%{?dist}
- ARGO-2017 - Token per tenants config option
- ARGO-2013 - Metric profiles WEB-API connector
- ARGO-1549 - New helper tool that can replay avro data on AMS with customizable datestamp
- ARGO-1575 - Switch poem-connector to use new token protected POEM API
* Wed Feb 20 2019 Daniel Vrcic <dvrcic@srce.hr> - 1.7.2-1%{?dist}
- ARGO-1674 Use requests library in connectors
* Fri Nov 30 2018 Daniel Vrcic <dvrcic@srce.hr>, Katarina Zailac <kzailac@srce.hr> - 1.7.1-1%{?dist}
- ARGO-1428 ServiceGroup topology filtering
- ARGO-1370 Optimize connectors queries to POEM
- ARGO-1269 Refactor poem-connector
- ARGO-1236 Datestamp of AMS msg does not match corresponding avro filename
* Wed May 23 2018 Daniel Vrcic <dvrcic@srce.hr> - 1.7.0-1%{?dist}
- ARGO-1093 Support for GOCDB paginated topology API
- ARGO-1080 add support for basic-auth in Connectors
- ARGO-966 Lower state files permissions
* Tue Mar 27 2018 Daniel Vrcic <dvrcic@srce.hr> - 1.6.1-1%{?dist}
- selectively use GOCDB paginated API for topology
* Thu Nov 30 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.6.0-1%{?dist}
- ARGO-965 Support for packing connectors data in a single AMS message
- ARGO-921 Use ComputationPower instead of HEPSPEC2006 value for weights
- ARGO-906 No explicit exit on connection problem so state file will be written
- ARGO-886 Finer retry logic
- ARGO-872 Tenant and jobname in retries log msgs
- ARGO-853 Connectors retry to fetch data
- ARGO-843 Write/send data as it is data for passed date
- ARGO-842 Connectors dedicated file logger
- ARGO-549 Use of AMS for delivering topology, downtimes, POEM profile and weights
- added unit tests
* Tue Apr 25 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.9-1%{?dist}
- ARGO-724 Each connector must try to create states directory structure
* Wed Mar 29 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.8-1%{?dist}
- ARGO-766 Remove SRMv2 service type mapping
* Mon Mar 20 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.7-1%{?dist}
- ARGO-767 Remove topology-vo connector
- refactored topology filtering
- removed schema migration helper
* Fri Mar 17 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.6-1%{?dist}
- ARGO-762 Remove inspection logic of HEPSPEC factors for previous days
* Thu Mar 9 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.5-1%{?dist}
- ARGO-713 Topology connector should be able to pick only particular NGI or site
* Mon Jan 30 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.4-1%{?dist}
- ARGO-667 filter endpoints whose groups are filtered in groups of groups
* Wed Jan 25 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.3-3%{?dist}
- prefilter output datestamp with underscores
* Wed Jan 25 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.3-2%{?dist}
- prefilter datestamp extracted from arg tuple
* Thu Jan 19 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.3-1%{?dist}
- poem and output files as arguments to prefilter
- refactored filename datestamp creation
* Wed Jan 4 2017 Daniel Vrcic <dvrcic@srce.hr> - 1.5.2-1%{?dist}
- ARGO-550 Introduce states that can be checked by Nagios probe
* Thu Nov 24 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.5.1-2%{?dist}
- remove code for nagioses defined in obsoleted nagios-roles.conf
- catch JSON parse errors
- catch XML parse errors
* Fri Oct 28 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.5.1-1%{?dist}
- ARGO-584 Ensure to catch all exceptions of underlying library
* Sat Sep 24 2016 Themis Zamani <themiszamani@gmail.com> - 1.5.0-1%{?dist}
- New RPM package release
* Wed Aug 31 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.4.6-2%{?dist}
- make use of VAPOR service for weights
- extended cert verification with CAfile bundle
* Tue Feb 16 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.4.6-1%{?dist}
- topology data without mixed int and string values
* Mon Feb 1 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.4.5-3%{?dist}
- poem connector optional write data needed for prefilter
  https://github.com/ARGOeu/ARGO/issues/184
* Tue Jan 12 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.4.5-2%{?dist}
- weights connector refactored
- README updated
  https://github.com/ARGOeu/ARGO/issues/181
* Sun Jan 10 2016 Daniel Vrcic <dvrcic@srce.hr> - 1.4.5-1%{?dist}
- log failed VO and weights connections
  https://github.com/ARGOeu/ARGO/issues/179
- added connection timeout for all connectors
- config files can be passed as arguments to every component
  https://github.com/ARGOeu/ARGO/issues/180
- added connection retry feature forr all connectors
- prefilter explicit input and output
- reorganized prefilter global.conf
- DATE placeholder in global.conf so interpolation can be used
- prefilter poem_sync.out look back option
- remove obsoleted logging
- guide updated
- refactored connection retries
* Thu Oct 15 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.4-6%{?dist}
- bugfix handling lowercase defined POEM profiles
- remove hardcoded customer name for topology-gocdb-connector
  https://github.com/ARGOeu/ARGO/issues/173
- guide updated with new configuration option for customer
* Thu Oct 8 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.4-5%{?dist}
- bugfix in case of no downtimes defined for given date
  https://github.com/ARGOeu/ARGO/issues/170
* Wed Oct 7 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.4-4%{?dist}
- poem-connector urlparse bugfix
* Wed Oct 7 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.4-3%{?dist}
- grab all distinct scopes for feed
* Tue Oct 6 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.4-2%{?dist}
- fix initialization of loggers in config parsers
- backward compatible exception messages
* Fri Oct 2 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.4-1%{?dist}
- filter SRM endpoints too
- refactored use of logging
- connectors can verify server certificate
  https://github.com/ARGOeu/ARGO/issues/153
- report correct number of fetched endpoints even if SRM endpoints were being filtered
- connectors handle help argument and describe basic info and usage
  https://github.com/ARGOeu/ARGO/issues/169
- removed hardcoded scopes and grab them dynamically from config
  https://github.com/ARGOeu/ARGO/issues/168
- report config parser errors via logger
- downtimes connector complain if wrong date specified
- remove notion of default scope
- doc moved to repo
- updated doc with server's cert validate options
* Wed Aug 19 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.3-3%{?dist}
- fix exception in case of returned HTTP 500 for other connectors
* Sat Aug 15 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.3-2%{?dist}
- fix poem-connector exception in case of returned HTTP 500
* Mon Aug 10 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.3-1%{?dist}
- generate meaningful statistic messages for every connector
- messages are written into syslog
  https://github.com/ARGOeu/ARGO/issues/116
* Wed Jul 15 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.2-2%{?dist}
- fixed bug with duplicating poem profiles info for prefilter
- fixed bug with SRM service type handling for topology and downtimes connectors
* Tue Jun 23 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.2-1%{?dist}
- changed internal parser structure to address entities with doubled scope
  https://github.com/ARGOeu/ARGO/issues/141
* Tue Jun 2 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.1-5%{?dist}
- new path and filename for consumer logs
* Thu May 28 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.1-4%{?dist}
- migrate.py lower on resources
* Thu May 21 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.1-3%{?dist}
- migration script to transform old data to new avro schema with map type
  https://github.com/ARGOeu/ARGO/issues/134
* Mon May 18 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.1-2%{?dist}
- GridPP VO job example
- downtimes filename day timestamp is queried one
  https://github.com/ARGOeu/ARGO/issues/133
* Wed May 6 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.1-1%{?dist}
- removed VO as an entity in configuration; only customers and set of jobs
- multiple customers in config each with own outputdir
- data feeds for all connectors can be defined per job
- prefilter-egi.py is aware of multiple customers
- avro schemas with generic tags
- case insensitive sections and options
- setup.py with automatic version catch from spec
- new default config
  https://github.com/ARGOeu/ARGO/issues/132
* Fri Apr 17 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-10%{?dist}
- VO jobs are moved under customer's directory
* Wed Apr 8 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-9%{?dist}
- handle group type names with whitespaces
- fixed bug with filtering VO groups across multiple VO jobs
* Fri Apr 3 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-8%{?dist}
- added Dirname optional option for VO config
- correctly renamed avro schemas
* Mon Mar 30 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-7%{?dist}
- added README.md with a basic project info
* Sun Mar 29 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-6%{?dist}
- renamed weights and more configs refactoring
- put scripts back into libexec
* Fri Mar 27 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-5%{?dist}
- minor code cleanups and renamed connectors to reflect the source of data
* Fri Mar 27 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-4%{?dist}
- poem server is defined in its config file, not global one
* Fri Mar 27 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-3%{?dist}
- prefilter-egi.py cleanups and roll back missing file
* Fri Mar 27 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-2%{?dist}
- deleted leftovers
* Fri Mar 27 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.4.0-1%{?dist}
- refactor the configuration of connectors/components
  https://github.com/ARGOeu/ARGO/issues/114
- fixed topology connector for VO'es to produce correct GE and GG avro files
  https://github.com/ARGOeu/ARGO/issues/121
- use of distutils for package building
* Tue Feb 17 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-16%{?dist}
- prefilter-avro has fixed configuration
* Thu Feb 12 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-15%{?dist}
- legacy SRM service type handle for downtime syncs
* Tue Feb 10 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-14%{?dist}
- updated .spec with removed configs for a per job prefilter-avro
* Tue Feb 10 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-13%{?dist}
- different internal handle of avro poem-sync so it doesn't contain duplicated entries
- special handle of legacy SRM service type
* Thu Feb 5 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-12%{?dist}
- plaintxt prefilter has fixed configuration
* Tue Feb 3 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-11%{?dist}
- update .spec to deploy new configs
- removed whitespaces at the end of config lines
* Mon Feb 2 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-10%{?dist}
- tools can have config file as their argument
- config files with changed output directory for customer/job
- modified cronjobs for customer and his two jobs
* Thu Jan 29 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-9%{?dist}
- bug fixes for poem-sync and prefilter
- typo in plaintext groups filename
* Mon Jan 19 2015 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-8%{?dist}
- topology-sync: avro schemas updated with tags and filtering by tags values
- poem-sync: avro schema updated with tags
- poem-sync: output profiles per customer and job
  https://github.com/ARGOeu/ARGO/issues/85
* Thu Jan 15 2015 Luko Gjenero <lgjenero@srce.hr> - 1.3.1-3%{?dist}
- avro prefiltering
* Wed Dec 17 2014 Daniel Vrcic <dvrcic@srce.hr> - 1.3.1-2%{?dist}
- ar-sync is missing avro dependency
- poem-sync is missing data for servers listed in URL
* Thu Nov 27 2014 Luko Gjenero <lgjenero@srce.hr> - 1.3.0-0%{?dist}
- Avro format for poem, downtimes, topology and hepspec
* Tue May 13 2014 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.2.3-1%{?dist}
- Added logging to sync components
* Fri Apr 26 2014 Luko Gjenero <lgjenero@srce.hr> - 1.2.2-1%{?dist}
- Updated prefilter
* Tue Mar 18 2014 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.2.1-1%{?dist}
- Updated daily cronjobs to run within first five minutes of each day
* Thu Jan 30 2014 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.1.19-1%{?dist}
- Updated daily cronjobs to run within first hour of each day
* Tue Jan 14 2014 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.1.18-1%{?dist}
- Added daily cronjob for hepspec values
* Thu Nov 28 2013 Luko Gjenero <lgjenero@srce.hr> - 1.1.16-3%{?dist}
- Fixed prefilter
* Thu Nov 28 2013 Luko Gjenero <lgjenero@srce.hr> - 1.1.16-2%{?dist}
- Fixed prefilter
* Thu Nov 28 2013 Luko Gjenero <lgjenero@srce.hr> - 1.1.16-1%{?dist}
- Updated prefilter
* Thu Nov 13 2013 Luko Gjenero <lgjenero@srce.hr> - 1.1.15-1%{?dist}
- VO Sync component
* Fri Nov 8 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.1.0-1%{?dist}
- Inclusion of hepspec sync plus cronjobs
* Mon Nov 4 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.0-6%{?dist}
- Fixes in consumer
* Tue Sep 17 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.0-5%{?dist}
- Fix in prefilter
* Mon Sep 9 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.0-4%{?dist}
- Rebuilt with fixed downtimes issue
* Thu Aug 29 2013 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.0-2%{?dist}
- Minor change in prefilter script
* Thu Aug 1 2013 Luko Gjenero <lgjenero@srce.hr> - 1.0.0-1%{?dist}
- Initial release

