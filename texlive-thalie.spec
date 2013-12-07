# revision 31018
# category Package
# catalog-ctan /macros/latex/contrib/thalie
# catalog-date 2013-06-19 11:30:49 +0200
# catalog-license lppl1.3
# catalog-version 0.5
Name:		texlive-thalie
Version:	0.5
Release:	4
Summary:	Typeset drama plays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thalie
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools to typeset drama plays. It defines
commands to introduce characters' lines, to render stage
directions, to divide a play into acts and scenes and to build
the dramatis personae automatically.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thalie/thalie.sty
%doc %{_texmfdistdir}/doc/latex/thalie/README
%doc %{_texmfdistdir}/doc/latex/thalie/thalie.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thalie/thalie.dtx
%doc %{_texmfdistdir}/source/latex/thalie/thalie.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
