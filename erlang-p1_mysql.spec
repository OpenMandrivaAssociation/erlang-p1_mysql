%global srcname p1_mysql
# Erlang packages do not provide debug subpackages
%global debug_package %{nil}


Name:       erlang-%{srcname}
Version:    1.0.1
Release:    %mkrel 1
Group:      Development/Java

Summary:    Pure Erlang MySQL driver
License:    BSD
URL:        https://github.com/processone/p1_mysql/
Source0:    https://github.com/processone/p1_mysql/archive/%{version}.tar.gz

BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros

Requires: erlang-erts


%description
This is an Erlang MySQL driver, used by ejabberd.


%prep
%autosetup -n p1_mysql-%{version}


%build
%rebar_compile

%check
%__rebar eunit

%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/include

install -pm644 ebin/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -pm644 include/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/include


%files
%license COPYING
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.1-1.mga6
+ Revision: 1068043
- New version 1.0.1

* Fri May 06 2016 neoclust <neoclust> 1.0.0-1.mga6
+ Revision: 1009904
- imported package erlang-p1_mysql

