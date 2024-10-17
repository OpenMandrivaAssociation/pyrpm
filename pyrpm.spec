Summary:	A rpm implementation purely in Python
Name:		pyrpm
Version:	0.70
Release:	%mkrel 7
License:	GPLv2+
Group:		System/Base
URL:		https://people.redhat.com/laroche/pyrpm/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	libpython-devel		>= 2.5
BuildRequires:	python-libxml2
Requires:	python-urlgrabber
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PyRPM is an experimental project to look at RPM package management. 
It is a Python module and a collection of scripts that provide similar 
functionality as rpm, yum, and related software.It can be used to study 
how rpm based software management happens. Also tools can build upon it 
to handle rpm packages in general e.g. to extract information, check 
dependencies or even install packages.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
mkdir -p %{buildroot}/var/cache/pyrpm

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*.html doc/*.txt
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_bindir}/old*
%attr(755,root,root) %{_bindir}/generate*
%attr(755,root,root) %{_bindir}/mpram*
%dir %{_datadir}/pyrpm
%dir %{_datadir}/pyrpm/pyrpm
%dir %{_datadir}/pyrpm/pyrpm/database
%dir %{_datadir}/pyrpm/pyrpm/installer
%{_datadir}/pyrpm/pyrpm/*.py*
%{_datadir}/pyrpm/pyrpm/database/*.py*
%{_datadir}/pyrpm/pyrpm/installer/*.py*
%{_var}/cache/pyrpm


%changelog
* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.70-7mdv2011.0
+ Revision: 653307
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.70-6mdv2010.0
+ Revision: 442003
- rebuild

* Tue Jan 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.70-5mdv2009.1
+ Revision: 331880
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.70-4mdv2009.0
+ Revision: 259470
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.70-3mdv2009.0
+ Revision: 247323
- rebuild

* Tue Jan 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.70-1mdv2008.1
+ Revision: 155999
- new version
- new license policy
- set default attributes for files

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.69-2mdv2008.0
+ Revision: 43002
- rebuild

* Mon May 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.69-1mdv2008.0
+ Revision: 24783
- new version

* Fri Apr 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.68-1mdv2008.0
+ Revision: 15944
- new version


* Tue Mar 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.65-1mdv2007.0
+ Revision: 133886
- new version

* Wed Feb 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.64-1mdv2007.1
+ Revision: 123434
- new version

* Thu Feb 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.63-1mdv2007.1
+ Revision: 117351
- Import pyrpm

