#
# spec file for package QNetWalk (Version 1.3)
#
# Copyright (c) 2008 Severin Leonhardt
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild

%define Werror_cflags %nil

Name:           qnetwalk
BuildRequires:  gcc
BuildRequires:  libqt4-devel
License:        GNU General Public License (GPL)
Group:          Games/Puzzles
Summary:        Game for System Administrators
Version:        1.3
Release:        7.17
URL:            http://qt.osdn.org.ua/qnetwalk.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-1.3_qtfix.diff

%description
This is a Qt-version of the popular NetWalk game for system administrators.
You have to connect all computers to the central server with as few clicks as possible.

Authors:
--------
    Andi Peredri <andi@ukr.net>

%prep
%setup -q
%patch0
%patch1 -p1

%build
qmake
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT $INSTALL_TARGET


%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_prefix}/games/qnetwalk
%{_datadir}/applications/qnetwalk.desktop
%{_mandir}/man6/qnetwalk.6.gz
%{_datadir}/pixmaps/qnetwalk.xpm
%dir %{_datadir}/games/qnetwalk/
%{_datadir}/games/qnetwalk/*

%changelog
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Thu May 15 2008 prusnak@suse.cz
- patched qmake project file (qnetwalk.patch)
- slightly modified spec file
* Mon Apr  7 2008 phoenixseve@gmx.de
- initial package created (version 1.3)
