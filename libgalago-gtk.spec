%define name libgalago-gtk
%define version 0.5.0
%define release %mkrel 8
%define major 1
%define libname %mklibname galago-gtk %major

Summary: Gtk bindings of Galago
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.galago-project.org/files/releases/source/libgalago-gtk/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: https://www.galago-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgalago-devel >= 0.5.0
BuildRequires: gtk+2-devel

%description
These are the gtk bindings of the Galago desktop presence framework.

%package -n %libname
Group: System/Libraries
Summary: Gtk bindings of Galago - shared library
#gw for the translations
Requires: %name >= %version

%description -n %libname
These are the gtk bindings of the Galago desktop presence framework.


%package -n %libname-devel
Group: Development/C
Summary: Gtk bindings of Galago - headers
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %libname-devel
These are the gtk bindings of the Galago desktop presence framework.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
rm -rf %buildroot%_datadir/autopackage
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS
%_datadir/pixmaps/galago/

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/%name.pc
%_includedir/%name/


