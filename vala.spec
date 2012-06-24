Summary:	GObject-based language compiler
Summary(pl):	Kompilator j�zyka opartego na bibliotece GObject
Name:		vala
Version:	0.0.1
Release:	0.1
License:	LGPL 2.1
Group:		Applications
Source0:	http://www.paldo.org/vala/%{name}-%{version}.tar.bz2
# Source0-md5:	c9b0916e6e091a115bc81ac552d19c10
URL:		http://www.paldo.org/vala/
BuildRequires:	glib2-devel >= 2.10.0
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

%description -l pl
Vala to nowy j�zyk programowania, kt�rego celem jest udost�pnienie
cech nowoczesnych j�zyk�w programowania programistom GNOME bez
wymuszania dodatkowych wymaga� co do �rodowiska uruchomieniowego i
u�ywania API innego ni� w aplikacjach i bibliotekach napisanych w C.

valac - kompilator j�zyka Vala - to napisany w sobie samym kompilator
t�umacz�cy kod �r�d�owy w j�zyku Vala na pliki �r�d�owe i nag��wkowe w
C. U�ywa systemu typ�w GObject do tworzenia klas i interfejs�w
zadeklarowanych w kodzie �r�d�owym w j�zyku Vala. Planowane jest tak�e
generowanie plik�w GIDL, kiedy system gobject-introspection b�dzie
gotowy.

Sk�adnia j�zyka Vala jest podobna do C#, zmodyfikowana tak, aby lepiej
pasowa� do systemu typ�w GObject.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vala
