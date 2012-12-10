Name:		delaboratory
Version:	0.8
Release:	2
Summary:	Free Software color correction utility
License:	GPLv3+
Group:		Graphics
Url:		https://code.google.com/p/delaboratory/
Source0:	https://delaboratory.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		delaboratory-0.8-mdv-makefile.patch
Requires:	dcraw
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
CXXFLAGS_WX="%{optflags}" ; export CXXFLAGS_WX ;
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




%changelog
* Tue Jul 31 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.8-2
+ Revision: 811500
- req dcraw for import RAW photos

* Mon Jul 30 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.8-1
+ Revision: 811390
- new version 0.8

* Wed Apr 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.7-1
+ Revision: 790299
- update to 0.7

* Fri Feb 17 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.6-1
+ Revision: 776159
- update to 0.6

* Thu Jan 19 2012 Andrey Bondrov <abondrov@mandriva.org> 0.5-2
+ Revision: 762299
- Rebuild against utf8 wxGTK2.8

* Fri Nov 11 2011 Andrey Smirnov <asmirnov@mandriva.org> 0.5-1
+ Revision: 730024
- imported package delaboratory

