Name:       acme.sh
Version:    {{version}}
Release:    1%{?dist}
Summary:    An ACME Shell script, a certbot client

Group:      Applications/System
URL:        https://github.com/Neilpang/acme.sh
Source0:    %{name}-%{version}.tar.gz

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

%description
An ACME Shell script, a certbot client: acme.sh https://acme.sh

%prep
%setup -q -n %{name}-%{version}

%build


%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

cp -av acme.sh %{_bindir}/%{name}


%changelog
