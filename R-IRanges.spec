%define		packname	IRanges

Summary:	Low-level containers for storing sets of integer ranges
Name:		R-%{packname}
Version:	1.20.6
Release:	2
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	4aa479a111bb6784b283ea56cde79012
URL:		http://bioconductor.org/packages/release/bioc/html/IRanges.html
BuildRequires:	R-BiocGenerics >= 0.5.6
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-BiocGenerics >= 0.5.6
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IRanges class and its extensions are low-level containers for
storing sets of integer ranges. A typical use of these containers in
biology is for representing a set of chromosome regions. More specific
extensions of the IRanges class will typically allow the storage of
additional information attached to each chromosome region as well as a
hierarchical relationship between these regions.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/unitTests

%files devel
%defattr(644,root,root,755)
%{_libdir}/R/library/%{packname}/include
