%define _disable_rebuild_configure 1

Summary:	A simple PolicyKit authentication agent
Name:		lxpolkit
Version:	0.1.0
Release:	13
Url:		https://www.lxde.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		lxpolkit-0.1.0-string-format.patch
License:	GPLv3+
Group:		System/Libraries
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	intltool
Provides:	polkit-agent
Requires:	polkit

%description
A simple PolicyKit authentication agent for LXDE.

%prep
%setup -q
%patch0 -p0 -b .str~

%build
%configure
%make

%install
%makeinstall_std

# make the polkit agent only start in LXDE
sed -i 's,NotShowIn=GNOME;KDE;,OnlyShowIn=LXDE;Old;,g' %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/%{name}.ui
