# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate proptest

Name:           rust-%{crate}0.10
Version:        0.10.1
Release:        3%{?dist}
Summary:        Hypothesis-like property-based testing and shrinking

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/proptest
Source:         %{crates_source}
# Initial patched metadata
# * exclude files that are only useful for upstream
Patch0:         proptest-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Hypothesis-like property-based testing and shrinking.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+atomic64bit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atomic64bit-devel %{_description}

This package contains library source intended for building other packages
which use "atomic64bit" feature of "%{crate}" crate.

%files       -n %{name}+atomic64bit-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bit-set-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bit-set-devel %{_description}

This package contains library source intended for building other packages
which use "bit-set" feature of "%{crate}" crate.

%files       -n %{name}+bit-set-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+break-dead-code-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+break-dead-code-devel %{_description}

This package contains library source intended for building other packages
which use "break-dead-code" feature of "%{crate}" crate.

%files       -n %{name}+break-dead-code-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+default-code-coverage-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-code-coverage-devel %{_description}

This package contains library source intended for building other packages
which use "default-code-coverage" feature of "%{crate}" crate.

%files       -n %{name}+default-code-coverage-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fork-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fork-devel %{_description}

This package contains library source intended for building other packages
which use "fork" feature of "%{crate}" crate.

%files       -n %{name}+fork-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+quick-error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quick-error-devel %{_description}

This package contains library source intended for building other packages
which use "quick-error" feature of "%{crate}" crate.

%files       -n %{name}+quick-error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-syntax-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-syntax-devel %{_description}

This package contains library source intended for building other packages
which use "regex-syntax" feature of "%{crate}" crate.

%files       -n %{name}+regex-syntax-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rusty-fork-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rusty-fork-devel %{_description}

This package contains library source intended for building other packages
which use "rusty-fork" feature of "%{crate}" crate.

%files       -n %{name}+rusty-fork-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tempfile-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tempfile-devel %{_description}

This package contains library source intended for building other packages
which use "tempfile" feature of "%{crate}" crate.

%files       -n %{name}+tempfile-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+timeout-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+timeout-devel %{_description}

This package contains library source intended for building other packages
which use "timeout" feature of "%{crate}" crate.

%files       -n %{name}+timeout-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

# building tests takes too much memory for 32-bit arches
%if %{with check} && %{?__isa_bits}%{?!__isa_bits:0} >= 64
%check
%cargo_test
%endif

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Fabio Valentini <decathorpe@gmail.com> - 0.10.1-1
- Initial compat package for proptest 0.10
