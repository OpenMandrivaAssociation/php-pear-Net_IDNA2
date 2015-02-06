%define		_class		Net
%define		_subclass	IDNA2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.1.1
Release:	5
Summary:	Punycode encoding and decoding
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_IDNA2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package helps you to encode and decode punycode strings easily.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-3mdv2012.0
+ Revision: 742145
- fix major breakage by careless packager
- delete one of them

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2
+ Revision: 679418
- mass rebuild

* Sat Jan 22 2011 Adam Williamson <awilliamson@mandriva.org> 0.1.1-1
+ Revision: 632388
- add source
- fix source extension
- imported package php-pear-Net_IDNA2

