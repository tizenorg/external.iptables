Name: iptables
Summary: administration tools for packet filtering and NAT
Version: 1.4.9.1
Release: 1
Source: %{name}-%{version}.tar.gz
Source1001: packaging/iptables.manifest 
Group: System/Base
URL: http://www.netfilter.org/
License: GPLv2
BuildRequires: kernel-headers
Conflicts: kernel < 2.4.20

%description
These are the user-space administration tools for the Linux
kernel's netfilter and iptables. netfilter and iptables provide
a framework for stateful and stateless packet filtering, network 
and port address translation, and other IP packet manipulation.
The framework is the successor to ipchains.
netfilter and iptables are used in applications such as Internet
connection sharing, firewalls, IP accounting, transparent proxying,
advanced routing and traffic control.

%package ipv6
Summary: IPv6 support for iptables
Group: System/Base
Requires: %{name} = %{version}-%{release}

%description ipv6
The iptables package contains IPv6 (the next version of the IP
protocol) support for iptables. Iptables controls the Linux kernel
network packet filtering code, allowing you to set up firewalls and IP
masquerading. 

Install iptables-ipv6 if you need to set up firewalling for your
network and you are using ipv6.

%package devel
Summary: development files for iptable's libipq
Group: System/Base
Requires: %{name} = %{version}-%{release}

%description devel
Header files, static libs and documentation for libipq, iptables'
user-space packet queuing library.

%prep
%setup -q

%build
cp %{SOURCE1001} .
%autogen
%configure --prefix=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT 

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest iptables.manifest
%defattr(-,root,root)
/usr/bin/iptables-xml
/usr/lib/libip4tc.so
/usr/lib/libip4tc.so.*
/usr/lib/libiptc.so
/usr/lib/libiptc.so.*
/usr/lib/libxtables.so
/usr/lib/libxtables.so.*
/usr/libexec/xtables/libipt*
/usr/libexec/xtables/libxt*
/usr/sbin/iptables*

%files ipv6
%manifest iptables.manifest
%defattr(-,root,root)
/usr/sbin/ip6tables*
/usr/lib/libip6tc.so
/usr/lib/libip6tc.so.*
/usr/libexec/xtables/libip6t*

%files devel
%manifest iptables.manifest
%defattr(-,root,root)
/usr/include/*
/usr/lib/*.la
/usr/lib/pkgconfig/*
%{_mandir}/man8/iptables*
%{_mandir}/man8/ip6tables*
