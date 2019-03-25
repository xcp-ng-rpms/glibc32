%define debug_package %{nil}
Summary: The GNU libc 32-bit libraries.
Name: glibc32
Version: 2.17
Release: 106.el7_2.4.2%dist
License: LGPL
# 32 bit binaries are extracted from the build RPMs directly
# The RPMs come from CentOS
Source0: glibc-2.17-106.el7_2.4.i686.rpm
Source1: glibc-devel-2.17-106.el7_2.4.i686.rpm
Source2: glibc-static-2.17-106.el7_2.4.i686.rpm
Source3: nss-softokn-freebl-3.16.2.3-13.el7_1.i686.rpm
ExclusiveArch: x86_64

BuildRequires: cpio
BuildRequires: genisoimage

%description
i686 libs for building x86_64 packages:
glibc, glibc-devel, glibc-static and nss-softokn-freebl

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
