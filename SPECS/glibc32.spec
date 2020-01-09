%define debug_package %{nil}
Summary: The GNU libc 32-bit libraries.
Name: glibc32
Version: 2.17
Release: 222.el7%dist
License: LGPL
# 32 bit binaries are extracted from the build RPMs directly
# The RPMs come from CentOS
# Version of glibc must match that of glibc in XCP-ng
# Version of nss-softokn-freebl must match that of the 64-bit build-dep
# (if there's one, else the version from the appropriate release of CentOS)
Source0: glibc-2.17-222.el7.i686.rpm
Source1: glibc-devel-2.17-222.el7.i686.rpm
Source2: glibc-static-2.17-222.el7.i686.rpm
Source3: nss-softokn-freebl-3.36.0-5.el7_5.i686.rpm
ExclusiveArch: x86_64

BuildRequires: cpio
BuildRequires: genisoimage

%description
i686 libs for building x86_64 packages:
glibc, glibc-devel, glibc-static and nss-softokn-freebl

%prep

%build
rpm2cpio %{SOURCE0} | cpio -idmv
rpm2cpio %{SOURCE1} | cpio -idmv
rpm2cpio %{SOURCE2} | cpio -idmv
rpm2cpio %{SOURCE3} | cpio -idmv

%install
cp -a * %{buildroot}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/lib/*
/usr/lib/*
/usr/include/*
%exclude /etc/*
%exclude /sbin/*
%exclude /usr/libexec/*
%exclude /usr/sbin/*
%exclude /usr/share/*
%exclude /var/*

%changelog
* Fri Dec 20 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.17-222.el7
- Rebuild for XCP-ng 8.1
- No changes
- Kept same revision number to match that of glibc
