%global tl_name thalie
%global tl_revision 65249

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.13a
Release:	%{tl_revision}.1
Summary:	Typeset drama plays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thalie
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thalie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools to typeset drama plays. It defines commands
to introduce characters' lines, to render stage directions, to divide a
play into acts and scenes and to build the dramatis personae
automatically.

