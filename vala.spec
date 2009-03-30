Summary:	GObject-based language compiler
Summary(pl.UTF-8):	Kompilator języka opartego na bibliotece GObject
Name:		vala
Version:	0.6.0
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vala/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	9e5888a79757eb0f47df118b39762ed6
URL:		http://www.paldo.org/vala/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-vapigen 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libvala.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvala.so.0
%attr(755,root,root) %{_libdir}/libvala.so
%{_libdir}/libvala.la
%{_includedir}/vala-1.0
%{_pkgconfigdir}/vala-1.0.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps
%{_mandir}/man1/valac.1*
%attr(755,root,root) %{_libdir}/vala/gen-introspect
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vapigen.1*

%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/vala
