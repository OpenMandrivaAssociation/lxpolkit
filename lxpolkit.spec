%define git git20100330

Summary:	A simple PolicyKit authentication agent
Name:		lxpolkit
Version:	0.1.0
Release:	%mkrel -c %git 2
Url:		http://www.lxde.org/
Source0:	%{name}-%{version}-%{git}.tar.bz2
Patch0:		lxpolkit-0.1.0-string-format.patch
License:	GPLv3+
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	polkit-1-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool

%description
A simple PolicyKit authentication agent for LXDE.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .str

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# make the polkit agent only start in LXDE
sed -i 's,NotShowIn=GNOME;KDE;,OnlyShowIn=LXDE,g' %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui/%{name}.ui
