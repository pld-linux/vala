#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build

%define	major_ver	0.56
Summary:	GObject-based language compiler
Summary(pl.UTF-8):	Kompilator języka opartego na bibliotece GObject
Name:		vala
Version:	0.56.2
Release:	1
Epoch:		2
License:	LGPL v2+
Group:		Development/Languages
Source0:	https://download.gnome.org/sources/vala/0.56/%{name}-%{version}.tar.xz
# Source0-md5:	de5d84b4941a834e2ed7983432220283
URL:		https://wiki.gnome.org/Projects/Vala
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.48.0
BuildRequires:	graphviz-devel >= 2.16
BuildRequires:	help2man
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
%{!?with_bootstrap:BuildRequires:	vala >= 2:0.39.5.8}
BuildRequires:	xz
Requires:	glib2 >= 1:2.48.0
Conflicts:	gdk-pixbuf2 < 2.23.3-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vala is a new programming language that aims to bring modern
programming language features to GNOME developers without imposing any
additional runtime requirements and without using a different ABI
compared to applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala
source code. It's also planned to generate GIDL files when
gobject-introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the
GObject type system.

%description -l pl.UTF-8
Vala to nowy język programowania, którego celem jest udostępnienie
cech nowoczesnych języków programowania programistom GNOME bez
wymuszania dodatkowych wymagań co do środowiska uruchomieniowego i
używania API innego niż w aplikacjach i bibliotekach napisanych w C.

valac - kompilator języka Vala - to napisany w sobie samym kompilator
tłumaczący kod źródłowy w języku Vala na pliki źródłowe i nagłówkowe w
C. Używa systemu typów GObject do tworzenia klas i interfejsów
zadeklarowanych w kodzie źródłowym w języku Vala. Planowane jest także
generowanie plików GIDL, kiedy system gobject-introspection będzie
gotowy.

Składnia języka Vala jest podobna do C#, zmodyfikowana tak, aby lepiej
pasować do systemu typów GObject.

%package apidocs
Summary:	vala API documentation
Summary(pl.UTF-8):	Dokumentacja API vala
Group:		Documentation
Requires:	devhelp
BuildArch:	noarch

%description apidocs
vala API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API vala.

%package -n valadoc
Summary:	Documentation tool for Vala
Summary(pl.UTF-8):	Narzędzie obsługujące dokumentację dla języka Vala
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n valadoc
Documentation tool for Vala.

%description -n valadoc -l pl.UTF-8
Narzędzie obsługujące dokumentację dla języka Vala.

%package -n valadoc-devel
Summary:	Header file for Valadoc library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Valadoc
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.48.0
Requires:	graphviz-devel >= 2.16
Requires:	valadoc = %{epoch}:%{version}-%{release}

%description -n valadoc-devel
Header file for Valadoc library.

%description -n valadoc-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Valadoc.

%package -n vala-valadoc
Summary:	Vala API for Valadoc library
Summary(pl.UTF-8):	API języka Vala do biblioteki Valadoc
Group:		Development/Libraries
Requires:	vala
Requires:	valadoc-devel = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description -n vala-valadoc
Vala API for Valadoc library.

%description -n vala-valadoc -l pl.UTF-8
API języka Vala do biblioteki Valadoc.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/vala/vapi

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/vala-*/lib*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/valadoc-*/doclets/*/libdoclet.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n valadoc -p /sbin/ldconfig
%postun	-n valadoc -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/vala
%attr(755,root,root) %{_bindir}/vala-%{major_ver}
%attr(755,root,root) %{_bindir}/vala-gen-introspect
%attr(755,root,root) %{_bindir}/vala-gen-introspect-%{major_ver}
%attr(755,root,root) %{_bindir}/valac
%attr(755,root,root) %{_bindir}/valac-%{major_ver}
%attr(755,root,root) %{_bindir}/vapigen
%attr(755,root,root) %{_bindir}/vapigen-%{major_ver}
%attr(755,root,root) %{_libdir}/libvala-%{major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvala-%{major_ver}.so.0
%attr(755,root,root) %{_libdir}/libvala-%{major_ver}.so
%{_includedir}/vala-%{major_ver}
%{_pkgconfigdir}/libvala-%{major_ver}.pc
%{_pkgconfigdir}/vapigen-%{major_ver}.pc
%{_pkgconfigdir}/vapigen.pc
%dir %{_datadir}/vala
%{_datadir}/vala/Makefile.vapigen
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libvala-%{major_ver}.vapi
%dir %{_datadir}/vala-%{major_ver}
%dir %{_datadir}/vala-%{major_ver}/vapi
%{_datadir}/vala-%{major_ver}/vapi/*.vapi
%{_datadir}/vala-%{major_ver}/vapi/*.deps
%dir %{_libdir}/vala-%{major_ver}
%attr(755,root,root) %{_libdir}/vala-%{major_ver}/gen-introspect-%{major_ver}
%attr(755,root,root) %{_libdir}/vala-%{major_ver}/libvalaccodegen.so
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{major_ver}.1*
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{major_ver}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{major_ver}.1*
%{_aclocaldir}/vala.m4
%{_aclocaldir}/vapigen.m4

%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/vala-%{major_ver}

%files -n valadoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/valadoc
%attr(755,root,root) %{_bindir}/valadoc-%{major_ver}
%attr(755,root,root) %{_libdir}/libvaladoc-%{major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvaladoc-%{major_ver}.so.0
%dir %{_libdir}/valadoc-%{major_ver}
%dir %{_libdir}/valadoc-%{major_ver}/doclets
%dir %{_libdir}/valadoc-%{major_ver}/doclets/devhelp
%attr(755,root,root) %{_libdir}/valadoc-%{major_ver}/doclets/devhelp/libdoclet.so
%dir %{_libdir}/valadoc-%{major_ver}/doclets/gtkdoc
%attr(755,root,root) %{_libdir}/valadoc-%{major_ver}/doclets/gtkdoc/libdoclet.so
%dir %{_libdir}/valadoc-%{major_ver}/doclets/html
%attr(755,root,root) %{_libdir}/valadoc-%{major_ver}/doclets/html/libdoclet.so
%{_datadir}/valadoc-%{major_ver}
%{_mandir}/man1/valadoc-%{major_ver}.1*
%{_mandir}/man1/valadoc.1*

%files -n valadoc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvaladoc-%{major_ver}.so
%{_includedir}/valadoc-%{major_ver}
%{_pkgconfigdir}/valadoc-%{major_ver}.pc

%files -n vala-valadoc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/valadoc-%{major_ver}.deps
%{_datadir}/vala/vapi/valadoc-%{major_ver}.vapi
