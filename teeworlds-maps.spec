Name:           teeworlds-maps
Version:        1.0.0
Release:        2%{?dist}
Summary:        Extra maps for Teeworlds

License:        Unknown
URL:            https://github.com/chuck-norris-network/teeworlds-maps-rpm
Source:         https://github.com/chuck-norris-network/%{name}-rpm/archive/%{version}.tar.gz

BuildArch:      noarch
Requires:       teeworlds-data

%description
Extra maps for Teeworlds, an online multi-player platform 2D shooter.

%prep
%setup

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/teeworlds/data

cp -pr maps/* %{buildroot}%{_datadir}/teeworlds/data

%files
%{_datadir}/teeworlds
