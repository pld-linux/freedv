Summary:        FreeDV Digital Voice
Summary(pl.UTF-8):	FreeDV Digital Voice - cyfrowy głos
Name:           freedv
Version:        1.3.1
Release:        1
License:        GPL v2+
Group:		X11/Applications/Sound
Source0:        https://hobbes1069.fedorapeople.org/freetel/%{name}/%{name}-%{version}.tar.xz
# Source0-md5:	43a4bca546def09662998509fe5c7abe
URL:            http://freedv.org/
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  codec2-devel >= 0.8.1
BuildRequires:  hamlib-devel >= 1.2.15.3
BuildRequires:  libsamplerate-devel >= 0.1.8
BuildRequires:  libsndfile-devel >= 1.0.25
BuildRequires:  libstdc++-devel
BuildRequires:  portaudio-devel >= 19
BuildRequires:  speexdsp-devel >= 1.2-0.rc3
BuildRequires:  wxGTK3-unicode-devel >= 3.0.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	codec2 >= 0.8.1
Requires:	hicolor-icon-theme
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
source software, released under the GNU Public License version 2.
The FDMDV modem and Codec 2 Speech codec used in FreeDV are also open
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
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DWXCONFIG=%{_bindir}/wx-gtk3-unicode-config \
	-DUSE_STATIC_CODEC2=OFF

%{__make}

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
%doc COPYING README.txt RELEASE_NOTES.txt USER_MANUAL.txt
%attr(755,root,root) %{_bindir}/freedv
%{_desktopdir}/freedv.desktop
%{_iconsdir}/hicolor/*x*/apps/freedv.png
