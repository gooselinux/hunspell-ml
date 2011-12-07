Name: hunspell-ml
Summary: Malayalam hunspell dictionaries
Version: 0.1
Release: 4.1%{?dist}
Source: http://download.savannah.gnu.org/releases/smc/Spellchecker/ooo-hunspell-ml-%{version}.tar.bz2
Group: Applications/Text
URL: http://download.savannah.gnu.org/releases/smc/Spellchecker/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch

Requires: hunspell

%description
Malayalam hunspell dictionaries

%prep
%setup -q -n ooo-hunspell-ml-%{version}

%build
echo "Nothing to build..."

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README  
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Parag <panemade@gmail.com> - 0.1-2
- Fix source md5sum 

* Thu May 15 2008 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> - 0.1-1
- Initial version
