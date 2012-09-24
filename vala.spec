%define	major_ver	0.18
Summary:	GObject-based language compiler
Summary(pl.UTF-8):	Kompilator języka opartego na bibliotece GObject
Name:		vala
Version:	0.18.0
Release:	1
Epoch:		2
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vala/0.18/%{name}-%{version}.tar.xz
# Source0-md5:	06a95d6a6466b3583b59fe956cc75486
URL:		http://live.gnome.org/Vala
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%description apidocs
vala API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API vala.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-vapigen
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/vala/vapi

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libvala-%{major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvala-%{major_ver}.so.0
%attr(755,root,root) %{_libdir}/libvala-%{major_ver}.so
%{_includedir}/vala-%{major_ver}
%{_pkgconfigdir}/libvala-%{major_ver}.pc
%{_npkgconfigdir}/vapigen-%{major_ver}.pc
%{_npkgconfigdir}/vapigen.pc
%dir %{_datadir}/vala
%{_datadir}/vala/Makefile.vapigen
%dir %{_datadir}/vala/vapi
%dir %{_datadir}/vala-%{major_ver}
%dir %{_datadir}/vala-%{major_ver}/vapi
%{_datadir}/vala-%{major_ver}/vapi/*.vapi
%{_datadir}/vala-%{major_ver}/vapi/*.deps
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{major_ver}.1*
%dir %{_libdir}/vala-%{major_ver}
%attr(755,root,root) %{_libdir}/vala-%{major_ver}/gen-introspect-%{major_ver}
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{major_ver}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{major_ver}.1*
%{_aclocaldir}/vala.m4
%{_aclocaldir}/vapigen.m4

%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/vala-%{major_ver}
