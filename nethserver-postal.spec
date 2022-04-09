Summary: NethServer postal integration
Name: nethserver-postal
Version: 1.0.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-docker, git, curl, jq

BuildRequires: perl
BuildRequires: nethserver-devtools

%description
NethServer Postal integration

%prep
%setup

%build
perl createlinks
mkdir -p root/var/lib/nethserver/postal

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/%{name}/

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a ui/* %{buildroot}/usr/share/cockpit/%{name}/

(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} \
  --dir /var/lib/nethserver/postal 'attr(755,root,root)' \
  --file /etc/sudoers.d/50_nsapi_nethserver_postal 'attr(0440,root,root)' \
  --file /usr/libexec/nethserver/api/%{name}/read 'attr(775,root,root)' \
%{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sun Apr 10 2022 Markus Neuberger <info@markusneuberger.at> - 1.0.0-1
- Init
- Fix services
- Add virtualhost and subdomain prop
- Add mailuser and mailpass prop
- Fix letsencrypt
- Fix application button
