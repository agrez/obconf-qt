%global     commit 41698c8e8a49f652d79f32f0f3b4a585560f29ce
%global     commit_short %(c=%{commit}; echo ${c:0:7})


Name:           obconf-qt
Version:        0.9.0
Release:        1.%{commit_short}%{?dist}
Summary:        Qt port of ObConf, a configuration editor for window manager OpenBox
License:        GPLv2+
URL:            https://github.com/lxde/obconf-qt
Source0:        https://github.com/lxde/obconf-qt/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit_short}.tar.gz
BuildRequires:  cmake
BuildRequires:  qt5-linguist
BuildRequires:  liblxqt-devel
BuildRequires:  openbox-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  libSM-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Gui)
Requires:       openbox


%description
ObConf-Qt is a Qt port of ObConf, a configuration editor for window manager OpenBox.
It is maintained by the LXQt project but can be used independently from this desktop environment.


%prep
%setup -n %{name}-%{commit}


%build
%{cmake_lxqt}
make %{?_smp_mflags}


%install
%{makeinstall} DESTDIR=%{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/%{name}.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
* Sat Sep 10 2016 Vaughan <devel at agrez dot net> - 0.9.0-1.41698c8
- initial package
