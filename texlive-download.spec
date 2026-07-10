%global tl_name download
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Allow LaTeX to download files using an external process
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/download
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/download.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/download.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/download.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to download files (using cURL or wget), from
within a document. To run the external commands, LaTeX (or whatever)
needs to be run with the --shell-escape flag; this creates a tension
between your needs and the security implications of the flag; users
should exercise due caution.

