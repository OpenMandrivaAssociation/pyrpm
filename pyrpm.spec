Summary:	A rpm implementation purely in Python
Name:		pyrpm
Version:	0.70
Release:	%mkrel 7
License:	GPLv2+
Group:		System/Base
URL:		http://people.redhat.com/laroche/pyrpm/
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
