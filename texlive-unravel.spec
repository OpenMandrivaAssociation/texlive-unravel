%global tl_name unravel
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3c
Release:	%{tl_revision}.1
Summary:	Watching TeX digest tokens
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unravel
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unravel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unravel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unravel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The aim of this LaTeX package is to help debug complicated macros. This
is done by letting the user step through the execution of some TeX code,
going through the details of nested expansions, performing assignments,
as well as some simple typesetting commands. To use this package, one
should normally run TeX in a terminal. The unravel package requires up-
to-date versions of the l3kernel, l3packages and l3experimental bundles.

