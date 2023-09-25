Summary:	FreeDV Digital Voice
Summary(pl.UTF-8):	FreeDV Digital Voice - cyfrowy głos
Name:		freedv
Version:	1.8.8.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Sound
#Source0Download: https://github.com/drowe67/freedv-gui/releases
Source0:	https://github.com/drowe67/freedv-gui/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	479cd8141a1f8e795a9f898e7fca2676
URL:		http://freedv.org/
BuildRequires:	alsa-lib-devel >= 1.1.8
BuildRequires:	cmake >= 3.13
BuildRequires:	codec2-devel >= 1.0.5
BuildRequires:	hamlib-devel >= 3.3
BuildRequires:	libsamplerate-devel >= 0.1.9
BuildRequires:	libsndfile-devel >= 1.0.28
BuildRequires:	libstdc++-devel
BuildRequires:	lpcnetfreedv-devel >= 0.3
BuildRequires:	portaudio-devel >= 19
BuildRequires:	speexdsp-devel >= 1.2-0.rc3
BuildRequires:	wxGTK3-unicode-devel >= 3.0.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	alsa-lib >= 1.1.8
Requires:	codec2 >= 1.0.5
Requires:	hamlib >= 3.3
Requires:	hicolor-icon-theme
Requires:	libsamplerate >= 0.1.9
Requires:	libsndfile >= 1.0.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeDV is a GUI application for Windows and Linux that allows any SSB
radio to be used for low bit rate digital voice.

Speech is compressed down to 1400 bit/s then modulated onto a 1100 Hz
wide QPSK signal which is sent to the Mic input of a SSB radio. On
receive, the signal is received by the SSB radio, then demodulated and
decoded by FreeDV.

FreeDV was built by an international team of Radio Amateurs working
together on coding, design, user interface and testing. FreeDV is open
source software, released under the GNU Public License version 2. The
FDMDV modem and Codec 2 Speech codec used in FreeDV are also open
source.

%description -l pl.UTF-8
FreeDV to graficzna aplikacja dla Windows i Linuksa pozwalająca na
używanie dowolnego radia SSB do przesyłania cyfrowego głosu z niskimi
współczynnikami prędkości.

Mowa jest kompresowana nawet do 1400 bitów/s, a następnie modulowana
sygnału QPSK o szerokości 1100 Hz, wysyłanego do wejścia mikrofonowego
radia SSB. W drugą stronę, sygnał jest odbierany przez radio SSB,
następnie demodulowany i dekodowany przez FreeDV.

FreeDV zostało stworzone przez międzynarodowy zespół radioamatorów
współpracujących przy kodowaniu, projektowaniu, interfejsie
użytkownika i testowaniu. Jest to oprogramowanie o otwartych źródłach,
wydane na licencji GNU Public License w wersji 2. Modem FDMDV oraz
kodek mowy Codec 2, używane we FreeDV, także mają otwarte źródła.

%prep
%setup -q -n freedv-gui-%{version}

%build
%cmake -B build \
	-DWXCONFIG=%{_bindir}/wx-gtk3-unicode-config

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README.md USER_MANUAL.md
%attr(755,root,root) %{_bindir}/freedv
%{_datadir}/freedv-gui
%{_desktopdir}/freedv.desktop
%{_iconsdir}/hicolor/*x*/apps/freedv.png
