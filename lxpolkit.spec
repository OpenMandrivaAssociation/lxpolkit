%define git git20110802

Summary:	A simple PolicyKit authentication agent
Name:		lxpolkit
Version:	0.1.0
Release:	2
Url:		http://www.lxde.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		lxpolkit-0.1.0-string-format.patch
License:	GPLv3+
Group:		System/Libraries
BuildRequires:	polkit-1-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
Provides:	polkit-agent

%description
A simple PolicyKit authentication agent for LXDE.

%prep
%setup -q
%patch0 -p0 -b .str~

%build
%configure2_5x
%make

%install
%makeinstall_std

# make the polkit agent only start in LXDE
sed -i 's,NotShowIn=GNOME;KDE;,OnlyShowIn=LXDE,g' %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui/%{name}.ui
