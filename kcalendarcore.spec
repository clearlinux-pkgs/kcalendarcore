#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kcalendarcore
Version  : 6.12.0
Release  : 73
URL      : https://download.kde.org/stable/frameworks/6.12/kcalendarcore-6.12.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.12/kcalendarcore-6.12.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.12/kcalendarcore-6.12.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0 LGPL-3.0
Requires: kcalendarcore-data = %{version}-%{release}
Requires: kcalendarcore-lib = %{version}-%{release}
Requires: kcalendarcore-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libical-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libical)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
To build these tests, build with the cmake option KDE4_BUILD_TESTS=ON.
To run all these tests, enter the command 'ctest'.
Details of failed tests are output to FAILED.log, and in the case of recurrence tests,
to the .out files equivalent to the .ref files containing the expected results.

%package data
Summary: data components for the kcalendarcore package.
Group: Data

%description data
data components for the kcalendarcore package.


%package dev
Summary: dev components for the kcalendarcore package.
Group: Development
Requires: kcalendarcore-lib = %{version}-%{release}
Requires: kcalendarcore-data = %{version}-%{release}
Provides: kcalendarcore-devel = %{version}-%{release}
Requires: kcalendarcore = %{version}-%{release}

%description dev
dev components for the kcalendarcore package.


%package lib
Summary: lib components for the kcalendarcore package.
Group: Libraries
Requires: kcalendarcore-data = %{version}-%{release}
Requires: kcalendarcore-license = %{version}-%{release}

%description lib
lib components for the kcalendarcore package.


%package license
Summary: license components for the kcalendarcore package.
Group: Default

%description license
license components for the kcalendarcore package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kcalendarcore-6.12.0
cd %{_builddir}/kcalendarcore-6.12.0
pushd ..
cp -a kcalendarcore-6.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742474332
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742474332
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalendarcore
cp %{_builddir}/kcalendarcore-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcalendarcore/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcalendarcore-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalendarcore/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcalendarcore-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalendarcore/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kcalendarcore.categories
/usr/share/qlogging-categories6/kcalendarcore.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KCalendarCore/KCalendarCore/Alarm
/usr/include/KF6/KCalendarCore/KCalendarCore/Attachment
/usr/include/KF6/KCalendarCore/KCalendarCore/Attendee
/usr/include/KF6/KCalendarCore/KCalendarCore/CalFilter
/usr/include/KF6/KCalendarCore/KCalendarCore/CalFormat
/usr/include/KF6/KCalendarCore/KCalendarCore/CalStorage
/usr/include/KF6/KCalendarCore/KCalendarCore/Calendar
/usr/include/KF6/KCalendarCore/KCalendarCore/CalendarListModel
/usr/include/KF6/KCalendarCore/KCalendarCore/CalendarPlugin
/usr/include/KF6/KCalendarCore/KCalendarCore/CalendarPluginLoader
/usr/include/KF6/KCalendarCore/KCalendarCore/Conference
/usr/include/KF6/KCalendarCore/KCalendarCore/CustomProperties
/usr/include/KF6/KCalendarCore/KCalendarCore/Duration
/usr/include/KF6/KCalendarCore/KCalendarCore/Event
/usr/include/KF6/KCalendarCore/KCalendarCore/Exceptions
/usr/include/KF6/KCalendarCore/KCalendarCore/FileStorage
/usr/include/KF6/KCalendarCore/KCalendarCore/FreeBusy
/usr/include/KF6/KCalendarCore/KCalendarCore/FreeBusyCache
/usr/include/KF6/KCalendarCore/KCalendarCore/FreeBusyPeriod
/usr/include/KF6/KCalendarCore/KCalendarCore/ICalFormat
/usr/include/KF6/KCalendarCore/KCalendarCore/Incidence
/usr/include/KF6/KCalendarCore/KCalendarCore/IncidenceBase
/usr/include/KF6/KCalendarCore/KCalendarCore/Journal
/usr/include/KF6/KCalendarCore/KCalendarCore/MemoryCalendar
/usr/include/KF6/KCalendarCore/KCalendarCore/OccurrenceIterator
/usr/include/KF6/KCalendarCore/KCalendarCore/Period
/usr/include/KF6/KCalendarCore/KCalendarCore/Person
/usr/include/KF6/KCalendarCore/KCalendarCore/Recurrence
/usr/include/KF6/KCalendarCore/KCalendarCore/RecurrenceRule
/usr/include/KF6/KCalendarCore/KCalendarCore/ScheduleMessage
/usr/include/KF6/KCalendarCore/KCalendarCore/Sorting
/usr/include/KF6/KCalendarCore/KCalendarCore/Todo
/usr/include/KF6/KCalendarCore/KCalendarCore/VCalFormat
/usr/include/KF6/KCalendarCore/KCalendarCore/Visitor
/usr/include/KF6/KCalendarCore/kcalendarcore/alarm.h
/usr/include/KF6/KCalendarCore/kcalendarcore/attachment.h
/usr/include/KF6/KCalendarCore/kcalendarcore/attendee.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calendar.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calendarlistmodel.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calendarplugin.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calendarpluginloader.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calfilter.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calformat.h
/usr/include/KF6/KCalendarCore/kcalendarcore/calstorage.h
/usr/include/KF6/KCalendarCore/kcalendarcore/conference.h
/usr/include/KF6/KCalendarCore/kcalendarcore/customproperties.h
/usr/include/KF6/KCalendarCore/kcalendarcore/duration.h
/usr/include/KF6/KCalendarCore/kcalendarcore/event.h
/usr/include/KF6/KCalendarCore/kcalendarcore/exceptions.h
/usr/include/KF6/KCalendarCore/kcalendarcore/filestorage.h
/usr/include/KF6/KCalendarCore/kcalendarcore/freebusy.h
/usr/include/KF6/KCalendarCore/kcalendarcore/freebusycache.h
/usr/include/KF6/KCalendarCore/kcalendarcore/freebusyperiod.h
/usr/include/KF6/KCalendarCore/kcalendarcore/icalformat.h
/usr/include/KF6/KCalendarCore/kcalendarcore/incidence.h
/usr/include/KF6/KCalendarCore/kcalendarcore/incidencebase.h
/usr/include/KF6/KCalendarCore/kcalendarcore/journal.h
/usr/include/KF6/KCalendarCore/kcalendarcore/kcalendarcore_export.h
/usr/include/KF6/KCalendarCore/kcalendarcore/memorycalendar.h
/usr/include/KF6/KCalendarCore/kcalendarcore/occurrenceiterator.h
/usr/include/KF6/KCalendarCore/kcalendarcore/period.h
/usr/include/KF6/KCalendarCore/kcalendarcore/person.h
/usr/include/KF6/KCalendarCore/kcalendarcore/recurrence.h
/usr/include/KF6/KCalendarCore/kcalendarcore/recurrencerule.h
/usr/include/KF6/KCalendarCore/kcalendarcore/schedulemessage.h
/usr/include/KF6/KCalendarCore/kcalendarcore/sorting.h
/usr/include/KF6/KCalendarCore/kcalendarcore/todo.h
/usr/include/KF6/KCalendarCore/kcalendarcore/vcalformat.h
/usr/include/KF6/KCalendarCore/kcalendarcore/visitor.h
/usr/include/KF6/KCalendarCore/kcalendarcore_version.h
/usr/lib64/cmake/KF6CalendarCore/FindLibIcal.cmake
/usr/lib64/cmake/KF6CalendarCore/KF6CalendarCoreConfig.cmake
/usr/lib64/cmake/KF6CalendarCore/KF6CalendarCoreConfigVersion.cmake
/usr/lib64/cmake/KF6CalendarCore/KF6CalendarCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6CalendarCore/KF6CalendarCoreTargets.cmake
/usr/lib64/libKF6CalendarCore.so
/usr/lib64/pkgconfig/KF6CalendarCore.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6CalendarCore.so.6.12.0
/V3/usr/lib64/qt6/qml/org/kde/calendarcore/libkcalendarcoreqml.so
/usr/lib64/libKF6CalendarCore.so.6
/usr/lib64/libKF6CalendarCore.so.6.12.0
/usr/lib64/qt6/qml/org/kde/calendarcore/kcalendarcoreqml.qmltypes
/usr/lib64/qt6/qml/org/kde/calendarcore/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/calendarcore/libkcalendarcoreqml.so
/usr/lib64/qt6/qml/org/kde/calendarcore/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalendarcore/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcalendarcore/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kcalendarcore/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
