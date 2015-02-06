Summary:	Game for System Administrators
Name:		qnetwalk
Version:	1.3
Release:	2
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://qt.osdn.org.ua/qnetwalk.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		qnetwalk-1.3-datapath.patch
Patch1:		qnetwalk-1.3_qtfix.diff
Patch2:		qnetwalk-1.3-sfmt.patch
Patch3:		qnetwalk-1.3-desktop.patch
BuildRequires:	qt4-devel

%description
This is a Qt-version of the popular NetWalk game for system administrators.
You have to connect all computers to the central server with as few clicks
as possible.

Authors:
--------
    Andi Peredri <andi@ukr.net>

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%doc COPYING ChangeLog README
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6.*
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*

