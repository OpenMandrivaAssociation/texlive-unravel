# revision 31307
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-unravel
Version:	20131009
Release:	8
Summary:	TeXLive unravel package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unravel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unravel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unravel.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive unravel package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/unravel/unravel.sty
%doc %{_texmfdistdir}/doc/latex/unravel/README
%doc %{_texmfdistdir}/doc/latex/unravel/unravel.pdf
#- source
%doc %{_texmfdistdir}/source/latex/unravel/unravel.dtx
%doc %{_texmfdistdir}/source/latex/unravel/unravel.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
