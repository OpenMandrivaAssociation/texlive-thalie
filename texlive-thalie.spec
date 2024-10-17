Name:		texlive-thalie
Version:	64664
Release:	2
Summary:	Typeset drama plays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thalie
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/thalie
%doc %{_texmfdistdir}/doc/latex/thalie
#- source
%doc %{_texmfdistdir}/source/latex/thalie

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
