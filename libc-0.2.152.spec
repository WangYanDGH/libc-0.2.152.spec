Name:           libc
Version:        0.2.152
Release:        2
Summary:        Raw FFI bindings to platforms' system libraries
License:        Apache License 
URL:            https://codeload.github.com/rust-lang/libc/tar.gz/refs/tags/0.2.152
Source:         %{name}-%{version}.tar.gz

%description
libc provides all of the definitions necessary to easily interoperate with C code (or "C-like" code) on each of the platforms that Rust supports. This includes type definitions (e.g. c_int), constants (e.g. EINVAL) as well as function headers (e.g. malloc).
%prep
tar -zxf %{_topdir}/SOURCES/%{name}-%{version}.tar.gz -C %{_buildrootdir}


%files



%changelog
* Mon Jan 15 2024  -3.1.0
- Add service

* Mon Jan 15 2024  -3.1.0
- Package init
