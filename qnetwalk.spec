Summary:	Game for System Administrators
Name:		qnetwalk
Version:	1.9.0
Release:	1
License:	GPLv2+
Group:		Games/Puzzles
URL:		https://github.com/AMDmi3/qnetwalk
Source0:	https://github.com/AMDmi3/qnetwalk/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		qnetwalk-1.9.0-datapath.patch
Patch1:		qnetwalk-1.9.0_qtfix.diff
Patch2:		qnetwalk-1.9.0-sfmt.patch
Patch3:		qnetwalk-1.9.0-desktop.patch
BuildSystem:	cmake
BuildOption:	-DUSE_QT6:BOOL=ON
BuildOption:	-DENABLE_SOUND:BOOL=ON
BuildOption:	-DENABLE_NLS:BOOL=ON
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6LinguistTools)

%description
This is a Qt-version of the popular NetWalk game for system administrators.
You have to connect all computers to the central server with as few clicks
as possible.

Authors:
--------
    Andi Peredri <andi@ukr.net>

%prep
%autosetup -p1

%files
%doc COPYING ChangeLog.md README.md
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6.*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/metainfo/%{name}.metainfo.xml
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
