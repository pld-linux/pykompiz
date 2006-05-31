Summary:	pyKompiz - a manager application for Compiz in KDE
Summary(de):	pyKompiz - in Aplikations Menager für Compiz in KDE
Summary(pl):	pyKompiz - mened¿er aplikacji dla Compiza w KDE
Name:		pykompiz
Version:	0.1.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.oakcourt.dyndns.org/projects/pykompiz/%{name}-%{version}.tar.gz
# Source0-md5:	5f396218d4f3c35c57fedd7f7a3e88cb
URL:		http://www.kde-apps.org/content/show.php?content=39783
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	python-PyKDE
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyKompiz is a manager application for Compiz in KDE. It is similar to
(and borrows code from) a Python script that was distributed with some
Compiz Debian packages. Features:

- switch between Kwin and Compiz for misbehaving applications.
- Invoke the gset-compiz tool to configure Compiz.
- Programmatically (DCOP) switch window managers
- DCOP: suspend and resume functions. See the documentation for
  details.
- remembers last active WM across sessions.

%description -l de
pyKompiz ist ein Aplikations Menager für Compiz in KDE.

%description -l pl
pyKompiz jest mened¿erem aplikacji dla Compiza w KDE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_iconsdir}/hicolor/22x22/apps}
install src/%{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}
install logo24.png $RPM_BUILD_ROOT%{_datadir}/%{name}/logo24.png
install logo24.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/apps/logo24.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*/*/apps/*.png
%{_datadir}/%{name}/*
