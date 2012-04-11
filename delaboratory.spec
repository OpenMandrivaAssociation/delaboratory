Name:		delaboratory
Version:	0.7
Release:	1
Summary:	Free Software color correction utility
License:	GPLv3+
Group:		Graphics
Url:		https://code.google.com/p/delaboratory/
Source0:	https://delaboratory.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		delaboratory-0.7-mdv-makefile.patch
BuildRequires:	tiff-devel
BuildRequires:	wxgtku-devel
BuildRequires:	libxml2-devel


%description
Delaboratory is a Free Software color correction utility, it allows you
to modify color/contrast of your photo in a creative way - by performing
non-destructive operations in different colorspaces (RGB/BW, XYZ/LAB/LCH,
CMY/CMYK, HSL/HSV) with floating-point precision per channel.

%prep
%setup -q
%patch0 -p1

%build
%setup_compile_flags
make DEBUG=YES

%install
install -D -m0755 delaboratory "%{buildroot}%{_bindir}/delaboratory"
install -d -m0755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Terminal=false
TryExec=delaboratory
Exec=delaboratory
Type=Application
Categories=Graphics;Photography;GTK;
StartupNotify=false
Name=Delaboratory
GenericName=Color correction utility
EOF

%files
%defattr(-,root,root)
%doc README
%{_bindir}/delaboratory
%{_datadir}/applications/%{name}.desktop


