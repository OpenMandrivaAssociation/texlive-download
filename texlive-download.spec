Name:		texlive-download
Version:	52257
Release:	2
Summary:	Allow LaTeX to download files using an external process
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/download
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/download.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/download.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/download.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to download files (using cURL or
wget), from within a document. To run the external commands,
LaTeX (or whatever) needs to be run with the --shell-escape
flag; this creates a tension between your needs and the
security implications of the flag; users should exercise due
caution.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/download/download.sty
%doc %{_texmfdistdir}/doc/latex/download/README
%doc %{_texmfdistdir}/doc/latex/download/download.pdf
#- source
%doc %{_texmfdistdir}/source/latex/download/download.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
