%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-q
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/omega.tar.xz
Source0295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/omega.doc.tar.xz
Source1243:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/norasi-c90.tar.xz
Source1499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notes2bib.tar.xz
Source1500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notes2bib.doc.tar.xz
Source1502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oscola.tar.xz
Source1503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oscola.doc.tar.xz
Source1855:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/old-arrows.tar.xz
Source1856:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/old-arrows.doc.tar.xz
Source1981:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/obnov.tar.xz
Source1982:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/obnov.doc.tar.xz
Source1983:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocherokee.tar.xz
Source1984:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocherokee.doc.tar.xz
Source1985:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocr-b.tar.xz
Source1986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocr-b.doc.tar.xz
Source1987:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocr-b-outline.tar.xz
Source1988:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocr-b-outline.doc.tar.xz
Source1990:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ogham.tar.xz
Source1991:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ogham.doc.tar.xz
Source1992:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oinuit.tar.xz
Source1993:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oinuit.doc.tar.xz
Source1995:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oldlatin.tar.xz
Source1996:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oldlatin.doc.tar.xz
Source1997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oldstandard.tar.xz
Source1998:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oldstandard.doc.tar.xz
Source2000:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/opensans.tar.xz
Source2001:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/opensans.doc.tar.xz
Source2003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/orkhun.tar.xz
Source2004:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/orkhun.doc.tar.xz
Source2005:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/overlock.tar.xz
Source2006:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/overlock.doc.tar.xz
Source2233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/othello.tar.xz
Source2234:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/othello.doc.tar.xz
Source2235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/othelloboard.tar.xz
Source2236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/othelloboard.doc.tar.xz
Source2314:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ofs.tar.xz
Source2315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ofs.doc.tar.xz
Source2945:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ntheorem-vn.doc.tar.xz
Source2981:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ordinalpt.tar.xz
Source2982:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ordinalpt.doc.tar.xz
Source3065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ntgclass.tar.xz
Source3066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ntgclass.doc.tar.xz
Source3212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numericplots.tar.xz
Source3213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numericplots.doc.tar.xz
Source4779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noconflict.tar.xz
Source4780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noconflict.doc.tar.xz
Source4781:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noindentafter.tar.xz
Source4782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noindentafter.doc.tar.xz
Source4783:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noitcrul.tar.xz
Source4784:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noitcrul.doc.tar.xz
Source4786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nolbreaks.tar.xz
Source4787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nolbreaks.doc.tar.xz
Source4788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nomencl.tar.xz
Source4789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nomencl.doc.tar.xz
Source4791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nomentbl.tar.xz
Source4792:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nomentbl.doc.tar.xz
Source4794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nonfloat.tar.xz
Source4795:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nonfloat.doc.tar.xz
Source4797:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nonumonpart.tar.xz
Source4798:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nonumonpart.doc.tar.xz
Source4800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nopageno.tar.xz
Source4801:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nopageno.doc.tar.xz
Source4802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notes.tar.xz
Source4803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notes.doc.tar.xz
Source4805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notoccite.tar.xz
Source4806:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notoccite.doc.tar.xz
Source4807:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nowidow.tar.xz
Source4808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nowidow.doc.tar.xz
Source4810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nox.tar.xz
Source4811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nox.doc.tar.xz
Source4812:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ntheorem.tar.xz
Source4813:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ntheorem.doc.tar.xz
Source4815:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numberedblock.tar.xz
Source4816:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numberedblock.doc.tar.xz
Source4817:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numname.tar.xz
Source4818:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numname.doc.tar.xz
Source4819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numprint.tar.xz
Source4820:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numprint.doc.tar.xz
Source4822:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocg-p.tar.xz
Source4823:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocg-p.doc.tar.xz
Source4824:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocgx.tar.xz
Source4825:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocgx.doc.tar.xz
Source4827:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocgx2.tar.xz
Source4828:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocgx2.doc.tar.xz
Source4829:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocr-latex.tar.xz
Source4830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ocr-latex.doc.tar.xz
Source4831:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/octavo.tar.xz
Source4832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/octavo.doc.tar.xz
Source4834:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oldstyle.tar.xz
Source4835:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oldstyle.doc.tar.xz
Source4837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/onlyamsmath.tar.xz
Source4838:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/onlyamsmath.doc.tar.xz
Source4840:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/opcit.tar.xz
Source4841:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/opcit.doc.tar.xz
Source4843:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/optional.tar.xz
Source4844:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/optional.doc.tar.xz
Source4845:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outline.tar.xz
Source4846:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outline.doc.tar.xz
Source4847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outliner.tar.xz
Source4848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outliner.doc.tar.xz
Source4849:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outlines.tar.xz
Source4850:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outlines.doc.tar.xz
Source4851:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/overpic.tar.xz
Source4852:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/overpic.doc.tar.xz
Source5810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/odsfile.tar.xz
Source5811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/odsfile.doc.tar.xz
Source5880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ot-tableau.tar.xz
Source5881:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ot-tableau.doc.tar.xz
Source5882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oubraces.tar.xz
Source5883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oubraces.doc.tar.xz
Source6072:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/otibet.tar.xz
Source6073:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/otibet.doc.tar.xz
Source6461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nostarch.tar.xz
Source6462:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nostarch.doc.tar.xz
Source6464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nrc.tar.xz
Source6465:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nrc.doc.tar.xz
Source6467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/onrannual.tar.xz
Source6468:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/onrannual.doc.tar.xz
Source6469:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/opteng.tar.xz
Source6470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/opteng.doc.tar.xz
Source6702:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nuc.tar.xz
Source6703:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nuc.doc.tar.xz
Source6704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/objectz.tar.xz
Source6705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/objectz.doc.tar.xz
Source7455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/normalcolor.tar.xz
Source7456:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/normalcolor.doc.tar.xz
Source7458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noto.tar.xz
Source7459:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/noto.doc.tar.xz
Source7460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nucleardata.tar.xz
Source7461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nucleardata.doc.tar.xz
Source7463:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nwejm.tar.xz
Source7464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nwejm.doc.tar.xz
Source7466:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/optidef.tar.xz
Source7467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/optidef.doc.tar.xz
Source7468:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/options.tar.xz
Source7469:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/options.doc.tar.xz
Source7874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nodetree.tar.xz
Source7875:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nodetree.doc.tar.xz
Source7876:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notespages.tar.xz
Source7877:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notespages.doc.tar.xz
Source7878:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notestex.tar.xz
Source7879:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notestex.doc.tar.xz
Source7880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/novel.tar.xz
Source7881:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/novel.doc.tar.xz
Source7882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numnameru.tar.xz
Source7883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numnameru.doc.tar.xz
Source7884:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numspell.tar.xz
Source7885:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/numspell.doc.tar.xz
Source7886:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/octave.tar.xz
Source7887:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/octave.doc.tar.xz
Source8042:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/olsak-misc.doc.tar.xz
Source8043:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/olsak-misc.tar.xz
Source8242:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/notex-bst.tar.xz
Source8246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/onedown.tar.xz
Source8247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/onedown.doc.tar.xz
Source8248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oplotsymbl.tar.xz
Source8249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oplotsymbl.doc.tar.xz
Source8250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outlining.tar.xz
Source8251:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/outlining.doc.tar.xz
Source8252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/overlays.tar.xz
Source8253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/overlays.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-norasi-c90
Provides:       tex-norasi-c90 = %{tl_version}
License:        LPPL
Summary:        TeX support (from CJK) for the norasi font
Version:        svn37675.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-fonts-tlwg
Provides:       tex(norasi-c90.map) = %{tl_version}, tex(ftnb8z.tfm) = %{tl_version}
Provides:       tex(ftnbi8z.tfm) = %{tl_version}, tex(ftni8z.tfm) = %{tl_version}
Provides:       tex(ftnr8z.tfm) = %{tl_version}

%description -n texlive-norasi-c90
norasi-c90 package

%package -n texlive-notes2bib
Provides:       tex-notes2bib = %{tl_version}
License:        LPPL
Summary:        Integrating notes into the bibliography
Version:        svn31162.2.0k

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xparse.sty), tex(l3keys2e.sty)
Provides:       tex(notes2bib.sty) = %{tl_version}

%description -n texlive-notes2bib
The package defines a new type of note, bibnote, which will
always be added to the bibliography. The package allows
footnotes and endnotes to be moved into the bibliography in the
same way. The package can be used with natbib and biblatex as
well as plain LaTeX citations. Both sorted and unsorted
bibliography styles are supported. The package uses the LaTeX 3
macros and the associated xpackages bundle. It also makes use
of the e-TeX extensions (any post-2005 LaTeX distribution will
provide these by default, but users of older systems may need
to use an elatex command or equivalent). The package relies on
LaTeX 3 support from the l3kernel and l3packages bundles.

%package -n texlive-notes2bib-doc
Summary:        Documentation for notes2bib
Version:        svn31162.2.0k

Provides:       tex-notes2bib-doc
AutoReqProv:    No

%description -n texlive-notes2bib-doc
Documentation for notes2bib

%package -n texlive-oscola
Provides:       tex-oscola = %{tl_version}
License:        LPPL 1.3
Summary:        BibLaTeX style for the Oxford Standard for the Citation of Legal Authorities
Version:        svn43599
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(authortitle.bbx), tex(verbose-inote.cbx)
Provides:       tex(oscola.bbx) = %{tl_version}, tex(oscola.cbx) = %{tl_version}

%description -n texlive-oscola
The package provides a set of style files for use with Biblatex
(v 2+) and Biber (v 1+) to produce citations and bibliographies
in accordance with the widely-used Oxford Standard for the
Citation of Legal Authorities. It also includes facilities for
constructing tables of cases and legislation from citations (in
conjunction with appropriate indexing packages).

%package -n texlive-oscola-doc
Summary:        Documentation for oscola
Version:        svn43599
Provides:       tex-oscola-doc
AutoReqProv:    No

%description -n texlive-oscola-doc
Documentation for oscola

%package -n texlive-old-arrows
Provides:       tex-old-arrows = %{tl_version}
License:        LPPL 1.3
Summary:        Computer Modern old-style arrows with smaller arrowheads
Version:        svn42872
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(oasy.enc) = %{tl_version}, tex(oasy.map) = %{tl_version}
Provides:       tex(oabsy10.tfm) = %{tl_version}, tex(oabsy5.tfm) = %{tl_version}
Provides:       tex(oabsy6.tfm) = %{tl_version}, tex(oabsy7.tfm) = %{tl_version}
Provides:       tex(oabsy8.tfm) = %{tl_version}, tex(oabsy9.tfm) = %{tl_version}
Provides:       tex(oasy10.tfm) = %{tl_version}, tex(oasy5.tfm) = %{tl_version}
Provides:       tex(oasy6.tfm) = %{tl_version}, tex(oasy7.tfm) = %{tl_version}
Provides:       tex(oasy8.tfm) = %{tl_version}, tex(oasy9.tfm) = %{tl_version}
Provides:       tex(oabsy10.pfb) = %{tl_version}, tex(oabsy5.pfb) = %{tl_version}
Provides:       tex(oabsy7.pfb) = %{tl_version}, tex(oasy10.pfb) = %{tl_version}
Provides:       tex(oasy5.pfb) = %{tl_version}, tex(oasy6.pfb) = %{tl_version}
Provides:       tex(oasy7.pfb) = %{tl_version}, tex(oasy8.pfb) = %{tl_version}
Provides:       tex(oasy9.pfb) = %{tl_version}, tex(old-arrows.sty) = %{tl_version}

%description -n texlive-old-arrows
This package provides Computer Modern old-style arrows with
smaller arrowheads, associated with the usual LaTeX commands.
It can be used in documents that contain other amssymb arrow
characters that also have small arrowheads. It is also possible
to use the usual new-style Computer Modern arrows together with
the old-style ones.

%package -n texlive-old-arrows-doc
Summary:        Documentation for old-arrows
Version:        svn42872
Provides:       tex-old-arrows-doc
AutoReqProv:    No

%description -n texlive-old-arrows-doc
Documentation for old-arrows

%package -n texlive-obnov
Provides:       tex-obnov = %{tl_version}
License:        LPPL
Summary:        Obyknovennaya Novaya fonts
Version:        svn33355.0.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(obn10.tfm) = %{tl_version}, tex(obn12.tfm) = %{tl_version}
Provides:       tex(obn17.tfm) = %{tl_version}, tex(obn7.tfm) = %{tl_version}
Provides:       tex(obnb10.tfm) = %{tl_version}, tex(obnb12.tfm) = %{tl_version}
Provides:       tex(obnb17.tfm) = %{tl_version}, tex(obnb7.tfm) = %{tl_version}
Provides:       tex(obnit10.tfm) = %{tl_version}, tex(obnit12.tfm) = %{tl_version}
Provides:       tex(obnit17.tfm) = %{tl_version}, tex(obnit7.tfm) = %{tl_version}
Provides:       tex(obnitb10.tfm) = %{tl_version}, tex(obnitb12.tfm) = %{tl_version}
Provides:       tex(obnitb17.tfm) = %{tl_version}, tex(obnsc10.tfm) = %{tl_version}
Provides:       tex(obnsc12.tfm) = %{tl_version}, tex(obnsc17.tfm) = %{tl_version}
Provides:       tex(obnsc7.tfm) = %{tl_version}, tex(obnsl10.tfm) = %{tl_version}
Provides:       tex(obnsl12.tfm) = %{tl_version}, tex(obnsl17.tfm) = %{tl_version}
Provides:       tex(obnsl7.tfm) = %{tl_version}, tex(lcywobn.fd) = %{tl_version}

%description -n texlive-obnov
The Obyknovennaya Novaya (Ordinary New Face) typeface was
widely used in the USSR for scientific and technical
publications, as well as textbooks. The fonts are encoded to
KOI8-R (which is a long-established Russian font encoding,
rather than a TeX/LaTeX encoding). To use the fonts, the user
needs Cyrillic font support.

%package -n texlive-obnov-doc
Summary:        Documentation for obnov
Version:        svn33355.0.11

Provides:       tex-obnov-doc
AutoReqProv:    No

%description -n texlive-obnov-doc
Documentation for obnov

%package -n texlive-ocherokee
Provides:       tex-ocherokee = %{tl_version}
License:        LPPL
Summary:        LaTeX Support for the Cherokee language
Version:        svn25689.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cherokee.map) = %{tl_version}, tex(Cherokee.tfm) = %{tl_version}
Provides:       tex(Cherokeeb.tfm) = %{tl_version}, tex(Cherokeebo.tfm) = %{tl_version}
Provides:       tex(Cherokeeo.tfm) = %{tl_version}, tex(Cherokee-Bold.pfb) = %{tl_version}
Provides:       tex(Cherokee.pfb) = %{tl_version}, tex(lchcmr.fd) = %{tl_version}
Provides:       tex(lchenc.def) = %{tl_version}, tex(ocherokee.sty) = %{tl_version}

%description -n texlive-ocherokee
Macros and Type 1 fonts for Typesetting the Cherokee language
with the Omega version of LaTeX (known as Lambda).

%package -n texlive-ocherokee-doc
Summary:        Documentation for ocherokee
Version:        svn25689.0

Provides:       tex-ocherokee-doc
AutoReqProv:    No

%description -n texlive-ocherokee-doc
Documentation for ocherokee

%package -n texlive-ocr-b
Provides:       tex-ocr-b = %{tl_version}
License:        Copyright only
Summary:        Fonts for OCR-B
Version:        svn20852.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ocrb10.tfm) = %{tl_version}, tex(ocrb5.tfm) = %{tl_version}
Provides:       tex(ocrb6.tfm) = %{tl_version}, tex(ocrb7.tfm) = %{tl_version}
Provides:       tex(ocrb8.tfm) = %{tl_version}, tex(ocrb9.tfm) = %{tl_version}

%description -n texlive-ocr-b
Metafont source for OCR-B at several sizes.

%package -n texlive-ocr-b-doc
Summary:        Documentation for ocr-b
Version:        svn20852.0

Provides:       tex-ocr-b-doc
AutoReqProv:    No

%description -n texlive-ocr-b-doc
Documentation for ocr-b

%package -n texlive-ocr-b-outline
Provides:       tex-ocr-b-outline = %{tl_version}
License:        Copyright only
Summary:        OCR-B fonts in Type 1 and OpenType
Version:        svn20969.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ocrb.map) = %{tl_version}, tex(ocrb10.otf) = %{tl_version}
Provides:       tex(ocrb5.otf) = %{tl_version}, tex(ocrb6.otf) = %{tl_version}
Provides:       tex(ocrb7.otf) = %{tl_version}, tex(ocrb8.otf) = %{tl_version}
Provides:       tex(ocrb9.otf) = %{tl_version}, tex(ocrb10.pfb) = %{tl_version}
Provides:       tex(ocrb5.pfb) = %{tl_version}, tex(ocrb6.pfb) = %{tl_version}
Provides:       tex(ocrb7.pfb) = %{tl_version}, tex(ocrb8.pfb) = %{tl_version}
Provides:       tex(ocrb9.pfb) = %{tl_version}

%description -n texlive-ocr-b-outline
The package contains OCR-B fonts in Type1 and OpenType formats.
They were generated from the Metafont sources of the OCR-B
fonts. The metric files are not included here, so that original
ocr-b package should also be installed.

%package -n texlive-ocr-b-outline-doc
Summary:        Documentation for ocr-b-outline
Version:        svn20969.0

Provides:       tex-ocr-b-outline-doc
AutoReqProv:    No

%description -n texlive-ocr-b-outline-doc
Documentation for ocr-b-outline

%package -n texlive-ogham
Provides:       tex-ogham = %{tl_version}
License:        Public Domain
Summary:        Fonts for typesetting Ogham script
Version:        svn24876.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ogham.tfm) = %{tl_version}

%description -n texlive-ogham
The font provides the Ogham alphabet, which is found on a
number of Irish and Pictish carvings dating from the 4th
century AD. The font is distributed as Metafont source, which
has been patched (with the author's permission) for stability
at different output device resolutions. (Thanks are due to
Peter Flynn and Dan Luecking.)

%package -n texlive-ogham-doc
Summary:        Documentation for ogham
Version:        svn24876.0

Provides:       tex-ogham-doc
AutoReqProv:    No

%description -n texlive-ogham-doc
Documentation for ogham

%package -n texlive-oinuit
Provides:       tex-oinuit = %{tl_version}
License:        LPPL
Summary:        LaTeX Support for the Inuktitut Language
Version:        svn28668.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(oinuit.map) = %{tl_version}, tex(Inuit.tfm) = %{tl_version}
Provides:       tex(Inuitb.tfm) = %{tl_version}, tex(Inuitbo.tfm) = %{tl_version}
Provides:       tex(Inuito.tfm) = %{tl_version}, tex(Inuit.pfb) = %{tl_version}
Provides:       tex(Inuitb.pfb) = %{tl_version}, tex(Inuitbo.pfb) = %{tl_version}
Provides:       tex(Inuito.pfb) = %{tl_version}, tex(cmssbxo10.pfb) = %{tl_version}
Provides:       tex(litcmr.fd) = %{tl_version}, tex(litenc.def) = %{tl_version}
Provides:       tex(oinuit.sty) = %{tl_version}

%description -n texlive-oinuit
The package provides a set of Lambda (Omega LaTeX) typesetting
tools for the Inuktitut language. Five different input methods
are supported and with the necessary fonts are also provided.

%package -n texlive-oinuit-doc
Summary:        Documentation for oinuit
Version:        svn28668.0

Provides:       tex-oinuit-doc
AutoReqProv:    No

%description -n texlive-oinuit-doc
Documentation for oinuit

%package -n texlive-oldlatin
Provides:       tex-oldlatin = %{tl_version}
License:        LPPL
Summary:        Compute Modern-like font with long s
Version:        svn17932.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(olb10.tfm) = %{tl_version}, tex(olbx10.tfm) = %{tl_version}
Provides:       tex(olbx12.tfm) = %{tl_version}, tex(olbx5.tfm) = %{tl_version}
Provides:       tex(olbx6.tfm) = %{tl_version}, tex(olbx7.tfm) = %{tl_version}
Provides:       tex(olbx8.tfm) = %{tl_version}, tex(olbx9.tfm) = %{tl_version}
Provides:       tex(olbxsl10.tfm) = %{tl_version}, tex(oldunh10.tfm) = %{tl_version}
Provides:       tex(olff10.tfm) = %{tl_version}, tex(olfib8.tfm) = %{tl_version}
Provides:       tex(olr10.tfm) = %{tl_version}, tex(olr12.tfm) = %{tl_version}
Provides:       tex(olr17.tfm) = %{tl_version}, tex(olr5.tfm) = %{tl_version}
Provides:       tex(olr6.tfm) = %{tl_version}, tex(olr7.tfm) = %{tl_version}
Provides:       tex(olr8.tfm) = %{tl_version}, tex(olr9.tfm) = %{tl_version}
Provides:       tex(olsl10.tfm) = %{tl_version}, tex(olsl12.tfm) = %{tl_version}
Provides:       tex(olsl8.tfm) = %{tl_version}, tex(olsl9.tfm) = %{tl_version}
Provides:       tex(olsltt10.tfm) = %{tl_version}, tex(olss10.tfm) = %{tl_version}
Provides:       tex(olss12.tfm) = %{tl_version}, tex(olss17.tfm) = %{tl_version}
Provides:       tex(olss8.tfm) = %{tl_version}, tex(olss9.tfm) = %{tl_version}
Provides:       tex(olssbx10.tfm) = %{tl_version}, tex(olssdc10.tfm) = %{tl_version}
Provides:       tex(olssi10.tfm) = %{tl_version}, tex(olssi12.tfm) = %{tl_version}
Provides:       tex(olssi17.tfm) = %{tl_version}, tex(olssi8.tfm) = %{tl_version}
Provides:       tex(olssi9.tfm) = %{tl_version}, tex(olssq8.tfm) = %{tl_version}
Provides:       tex(olssqi8.tfm) = %{tl_version}, tex(oltt10.tfm) = %{tl_version}
Provides:       tex(oltt12.tfm) = %{tl_version}, tex(oltt8.tfm) = %{tl_version}
Provides:       tex(oltt9.tfm) = %{tl_version}, tex(olvtt10.tfm) = %{tl_version}

%description -n texlive-oldlatin
Metafont sources modified from Computer Modern in order to
generate "long s" which was used in old text.

%package -n texlive-oldlatin-doc
Summary:        Documentation for oldlatin
Version:        svn17932.1.00

Provides:       tex-oldlatin-doc
AutoReqProv:    No

%description -n texlive-oldlatin-doc
Documentation for oldlatin

%package -n texlive-oldstandard
Provides:       tex-oldstandard = %{tl_version}
License:        OFL
Summary:        Old Standard: A Unicode Font for Classical and Medieval Studies
Version:        svn41735
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       oldstandard-sfd-fonts
Provides:       tex(OldStandard-Bold.otf) = %{tl_version}
Provides:       tex(OldStandard-Italic.otf) = %{tl_version}
Provides:       tex(OldStandard-Regular.otf) = %{tl_version}

%description -n texlive-oldstandard
Old Standard is designed to reproduce the actual printing style
of the early 20th century, reviving a specific type of Modern
(classicist) style of serif typefaces, very commonly used in
various editions of the late 19th and early 20th century, but
almost completely abandoned later. The font supports
typesetting of Old and Middle English, Old Icelandic, Cyrillic
(with historical characters, extensions for Old Slavonic and
localised forms), Gothic transliterations, critical editions of
Classical Greek and Latin, and many more. Old Standard works
with TeX engines that directly support OpenType features, such
as XeTeX and LuaTeX.

%package -n texlive-oldstandard-doc
Summary:        Documentation for oldstandard
Version:        svn41735
Provides:       tex-oldstandard-doc
AutoReqProv:    No

%description -n texlive-oldstandard-doc
Documentation for oldstandard

%package -n texlive-opensans
Provides:       tex-opensans = %{tl_version}
License:        LPPL 1.3
Summary:        The Open Sans font family, and LaTeX support
Version:        svn24706.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty), tex(slantsc.sty)
Provides:       tex(opensans-01.enc) = %{tl_version}, tex(opensans-02.enc) = %{tl_version}
Provides:       tex(opensans-03.enc) = %{tl_version}, tex(opensans-04.enc) = %{tl_version}
Provides:       tex(opensans.map) = %{tl_version}, tex(OpenSans-Bold-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLight-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Italic-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Light-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Regular-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-Semibold-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-01.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-02.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-03.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-04.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-lgr.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t2a.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t2b.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t2c.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-ts1.tfm) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-x2.tfm) = %{tl_version}
Provides:       tex(OpenSans-Bold.ttf) = %{tl_version}, tex(OpenSans-BoldItalic.ttf) = %{tl_version}
Provides:       tex(OpenSans-CondLight.ttf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic.ttf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold.ttf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic.ttf) = %{tl_version}
Provides:       tex(OpenSans-Italic.ttf) = %{tl_version}
Provides:       tex(OpenSans-Light.ttf) = %{tl_version}, tex(OpenSans-LightItalic.ttf) = %{tl_version}
Provides:       tex(OpenSans-Regular.ttf) = %{tl_version}
Provides:       tex(OpenSans-Semibold.ttf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic.ttf) = %{tl_version}
Provides:       tex(OpenSans-Bold.pfb) = %{tl_version}, tex(OpenSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(OpenSans-CondLight.pfb) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic.pfb) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold.pfb) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(OpenSans-Italic.pfb) = %{tl_version}
Provides:       tex(OpenSans-Light.pfb) = %{tl_version}, tex(OpenSans-LightItalic.pfb) = %{tl_version}
Provides:       tex(OpenSans-Regular.pfb) = %{tl_version}
Provides:       tex(OpenSans-Semibold.pfb) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic.pfb) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-Bold-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-BoldItalic-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLight-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-CondLightItalic-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBold-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-ExtraBoldItalic-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-Italic-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-Light-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-LightItalic-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-Regular-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-Semibold-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-OSFigures-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-lgr.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-ot1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t2a.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t2b.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-t2c.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-ts1.vf) = %{tl_version}
Provides:       tex(OpenSans-SemiboldItalic-x2.vf) = %{tl_version}
Provides:       tex(lgrfos.fd) = %{tl_version}, tex(lgrfosj.fd) = %{tl_version}
Provides:       tex(opensans.sty) = %{tl_version}, tex(ot1fos.fd) = %{tl_version}
Provides:       tex(ot1fosj.fd) = %{tl_version}, tex(t1fos.fd) = %{tl_version}
Provides:       tex(t1fosj.fd) = %{tl_version}, tex(t2afos.fd) = %{tl_version}
Provides:       tex(t2afosj.fd) = %{tl_version}, tex(t2bfos.fd) = %{tl_version}
Provides:       tex(t2bfosj.fd) = %{tl_version}, tex(t2cfos.fd) = %{tl_version}
Provides:       tex(t2cfosj.fd) = %{tl_version}, tex(ts1fos.fd) = %{tl_version}
Provides:       tex(ts1fosj.fd) = %{tl_version}, tex(x2fos.fd) = %{tl_version}
Provides:       tex(x2fosj.fd) = %{tl_version}

%description -n texlive-opensans
Open Sans is a humanist sans serif typeface designed by Steve
Matteson; the font is available from the Google Font Directory
as TrueType files licensed under the Apache License version
2.0. The package provides support for this font family in
LaTeX. It includes the original TrueType fonts, as well as Type
1 versions, converted for this package using FontForge for full
support with dvips

%package -n texlive-opensans-doc
Summary:        Documentation for opensans
Version:        svn24706.1.2

Provides:       tex-opensans-doc
AutoReqProv:    No

%description -n texlive-opensans-doc
Documentation for opensans

%package -n texlive-orkhun
Provides:       tex-orkhun = %{tl_version}
License:        LPPL
Summary:        A font for orkhun script
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(orhant11.tfm) = %{tl_version}, tex(orhant14.tfm) = %{tl_version}
Provides:       tex(orhant16.tfm) = %{tl_version}, tex(orhant20.tfm) = %{tl_version}
Provides:       tex(orhant25.tfm) = %{tl_version}

%description -n texlive-orkhun
The font covers an old Turkic script. It is provided as
Metafont source.

%package -n texlive-orkhun-doc
Summary:        Documentation for orkhun
Version:        svn15878.0

Provides:       tex-orkhun-doc
AutoReqProv:    No

%description -n texlive-orkhun-doc
Documentation for orkhun

%package -n texlive-overlock
Provides:       tex-overlock = %{tl_version}
License:        OFL
Summary:        Overlook sans fonts with LaTeX support
Version:        svn34409.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(ovlk_47cn4f.enc) = %{tl_version}, tex(ovlk_aqjbqj.enc) = %{tl_version}
Provides:       tex(ovlk_fvk6cm.enc) = %{tl_version}, tex(ovlk_irzqhk.enc) = %{tl_version}
Provides:       tex(ovlk_k6z3ge.enc) = %{tl_version}, tex(ovlk_u2ziis.enc) = %{tl_version}
Provides:       tex(ovlk_y3zmsf.enc) = %{tl_version}, tex(ovlk_yaegef.enc) = %{tl_version}
Provides:       tex(overlock.map) = %{tl_version}, tex(Overlock-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Overlock-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Overlock-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(Overlock-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Overlock-Black.ttf) = %{tl_version}, tex(Overlock-BlackItalic.ttf) = %{tl_version}
Provides:       tex(Overlock-Bold.ttf) = %{tl_version}, tex(Overlock-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Overlock-Italic.ttf) = %{tl_version}
Provides:       tex(Overlock-Regular.ttf) = %{tl_version}
Provides:       tex(OverlockSC-Regular.ttf) = %{tl_version}
Provides:       tex(Overlock-Black.pfb) = %{tl_version}, tex(Overlock-BlackItalic.pfb) = %{tl_version}
Provides:       tex(Overlock-Bold.pfb) = %{tl_version}, tex(Overlock-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Overlock-Italic.pfb) = %{tl_version}
Provides:       tex(Overlock-Regular.pfb) = %{tl_version}
Provides:       tex(OverlockSC-Regular.pfb) = %{tl_version}
Provides:       tex(Overlock-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(Overlock-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(Overlock-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Overlock-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Overlock-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Overlock-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Overlock-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Overlock-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(OverlockSC-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Overlock-LF.fd) = %{tl_version}, tex(LY1OverlockSC-LF.fd) = %{tl_version}
Provides:       tex(OT1Overlock-LF.fd) = %{tl_version}, tex(OT1OverlockSC-LF.fd) = %{tl_version}
Provides:       tex(T1Overlock-LF.fd) = %{tl_version}, tex(T1OverlockSC-LF.fd) = %{tl_version}
Provides:       tex(TS1Overlock-LF.fd) = %{tl_version}, tex(TS1OverlockSC-LF.fd) = %{tl_version}
Provides:       tex(overlock.sty) = %{tl_version}

%description -n texlive-overlock
The package provides the Overlock and OverlockSC families of
fonts, designed by Dario Manuel Muhafara of the TIPO foundry
(http://www.tipo.net.ar) are "rounded" sans-serif fonts in
three weights (Regular, Bold, Black) with italic variants for
each of them. There are also small-caps and old-style figures
in the Regular weight.

%package -n texlive-overlock-doc
Summary:        Documentation for overlock
Version:        svn34409.0

Provides:       tex-overlock-doc
AutoReqProv:    No

%description -n texlive-overlock-doc
Documentation for overlock

%package -n texlive-othello
Provides:       tex-othello = %{tl_version}
License:        GPL+
Summary:        Modification of a Go package to create othello boards
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ot10.tfm) = %{tl_version}, tex(ot15.tfm) = %{tl_version}
Provides:       tex(ot1bla10.tfm) = %{tl_version}, tex(ot1bla15.tfm) = %{tl_version}
Provides:       tex(ot1bla20.tfm) = %{tl_version}, tex(ot1neu10.tfm) = %{tl_version}
Provides:       tex(ot1neu15.tfm) = %{tl_version}, tex(ot1neu20.tfm) = %{tl_version}
Provides:       tex(ot1whi10.tfm) = %{tl_version}, tex(ot1whi15.tfm) = %{tl_version}
Provides:       tex(ot1whi20.tfm) = %{tl_version}, tex(othello.sty) = %{tl_version}

%description -n texlive-othello
A package (based on Kolodziejska's go), and fonts (as Metafont
source) are provided.

%package -n texlive-othello-doc
Summary:        Documentation for othello
Version:        svn15878.0

Provides:       tex-othello-doc
AutoReqProv:    No

%description -n texlive-othello-doc
Documentation for othello

%package -n texlive-othelloboard
Provides:       tex-othelloboard = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Othello (Reversi) diagrams of any size, with annotations
Version:        svn23714.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(pict2e.sty), tex(ifthen.sty), tex(color.sty)
Requires:       tex(xstring.sty), tex(stringstrings.sty)
Provides:       tex(othelloboard.sty) = %{tl_version}

%description -n texlive-othelloboard
The package enables the user to generate high-quality Othello
(also known as Reversi) board diagrams of any size. The
diagrams support annotations, including full game transcripts.
Automated board or transcript creation, from plain text formats
standard to WZebra (and other programs) is also supported.

%package -n texlive-othelloboard-doc
Summary:        Documentation for othelloboard
Version:        svn23714.1.2

Provides:       tex-othelloboard-doc
AutoReqProv:    No

%description -n texlive-othelloboard-doc
Documentation for othelloboard

%package -n texlive-ofs
Provides:       tex-ofs = %{tl_version}
License:        Knuth
Summary:        Macros for managing large font collections
Version:        svn16991.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(a117.tex) = %{tl_version}, tex(a35.sty) = %{tl_version}
Provides:       tex(a35.tex) = %{tl_version}, tex(allfonts.sty) = %{tl_version}
Provides:       tex(allfonts.tex) = %{tl_version}, tex(amsfn.tex) = %{tl_version}
Provides:       tex(mtfn.tex) = %{tl_version}, tex(ofs-6a.tex) = %{tl_version}
Provides:       tex(ofs-6c.tex) = %{tl_version}, tex(ofs-6k.tex) = %{tl_version}
Provides:       tex(ofs-6s.tex) = %{tl_version}, tex(ofs-6t.tex) = %{tl_version}
Provides:       tex(ofs-6x.tex) = %{tl_version}, tex(ofs-6y.tex) = %{tl_version}
Provides:       tex(ofs-8c.tex) = %{tl_version}, tex(ofs-8t.tex) = %{tl_version}
Provides:       tex(ofs-8x.tex) = %{tl_version}, tex(ofs-8z.tex) = %{tl_version}
Provides:       tex(ofs-ams.tex) = %{tl_version}, tex(ofs-cm.tex) = %{tl_version}
Provides:       tex(ofs-mt.tex) = %{tl_version}, tex(ofs-ps.tex) = %{tl_version}
Provides:       tex(ofs-px.tex) = %{tl_version}, tex(ofs-slt.tex) = %{tl_version}
Provides:       tex(ofs-tx.tex) = %{tl_version}, tex(ofs.sty) = %{tl_version}
Provides:       tex(ofs.tex) = %{tl_version}, tex(ofsdef.tex) = %{tl_version}
Provides:       tex(pantyk.tex) = %{tl_version}, tex(txfn.tex) = %{tl_version}

%description -n texlive-ofs
OFS (Olsak's Font System) is a set of Plain TeX and LaTeX
macros for managing large font collections; it has been used by
Czech/Slovak users for many years. Main features include:
Mapping from long names of fonts to the metric file name. The
user can specify only exact long names in documents. Support
for many font encodings. Printing of catalogues of fonts and
test samples of font families; the interactive macro \showfonts
shows all font families you have installed via OFS. The user
interface is the same for Plain TeX and for LaTeX, but the
implementation differs: the LaTeX variant of OFS uses NFSS, but
the Plain variant implements its own font management (which may
even be better than NFSS) Support for math fonts including TX
fonts.

%package -n texlive-ofs-doc
Summary:        Documentation for ofs
Version:        svn16991.0

Provides:       tex-ofs-doc
AutoReqProv:    No

%description -n texlive-ofs-doc
Documentation for ofs

%package -n texlive-ntheorem-vn-doc
Summary:        Documentation for ntheorem-vn
Version:        svn15878.1.203

Provides:       tex-ntheorem-vn-doc
AutoReqProv:    No

%description -n texlive-ntheorem-vn-doc
Documentation for ntheorem-vn

%package -n texlive-ordinalpt
Provides:       tex-ordinalpt = %{tl_version}
License:        LPPL
Summary:        Counters as ordinal numbers in Portuguese
Version:        svn15878.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ordinalpt.sty) = %{tl_version}

%description -n texlive-ordinalpt
The package provides a counter style (like \arabic, \alph and
others) which produces as output strings like "primeiro"
("first" in Portuguese), "segundo" (second), and so on up to
1999th. Separate counter commands are provided for different
letter case variants, and for masculine and feminine gender
inflections.

%package -n texlive-ordinalpt-doc
Summary:        Documentation for ordinalpt
Version:        svn15878.2.1

Provides:       tex-ordinalpt-doc
AutoReqProv:    No

%description -n texlive-ordinalpt-doc
Documentation for ordinalpt

%package -n texlive-ntgclass
Provides:       tex-ntgclass = %{tl_version}
License:        LPPL 1.3
Summary:        "European" versions of standard classes
Version:        svn15878.2.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(a4.sty) = %{tl_version}, tex(artikel1.cls) = %{tl_version}
Provides:       tex(artikel2.cls) = %{tl_version}, tex(artikel3.cls) = %{tl_version}
Provides:       tex(boek.cls) = %{tl_version}, tex(boek3.cls) = %{tl_version}
Provides:       tex(brief.cls) = %{tl_version}, tex(ntg10.clo) = %{tl_version}
Provides:       tex(ntg11.clo) = %{tl_version}, tex(ntg12.clo) = %{tl_version}
Provides:       tex(rapport1.cls) = %{tl_version}, tex(rapport3.cls) = %{tl_version}

%description -n texlive-ntgclass
The bundle offers versions of the standard LaTeX article and
report classes, rewritten to reflect a more European design,
and the a4 package, which is better tuned to the shape of a4
paper than is the a4paper class option of the standard classes.
The classes include several for article and report
requirements, and a letter class. The elements of the bundle
were designed by members of the Dutch TeX Users Group NTG.

%package -n texlive-ntgclass-doc
Summary:        Documentation for ntgclass
Version:        svn15878.2.1a

Provides:       tex-ntgclass-doc
AutoReqProv:    No

%description -n texlive-ntgclass-doc
Documentation for ntgclass

%package -n texlive-numericplots
Provides:       tex-numericplots = %{tl_version}
License:        GPLv3+
Summary:        Plot numeric data (including Matlab export) using PSTricks
Version:        svn31729.2.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(fp.sty), tex(ifthen.sty), tex(pstricks.sty)
Requires:       tex(pst-node.sty), tex(pst-plot.sty), tex(pstricks-add.sty), tex(xcolor.sty)
Requires:       tex(xkeyval.sty), tex(xkvview.sty)
Provides:       tex(NumericPlots.sty) = %{tl_version}, tex(NumericPlots_TickLabels.tex) = %{tl_version}
Provides:       tex(NumericPlots_labels.tex) = %{tl_version}
Provides:       tex(NumericPlots_legend.tex) = %{tl_version}
Provides:       tex(NumericPlots_macros.tex) = %{tl_version}
Provides:       tex(NumericPlots_styles.tex) = %{tl_version}

%description -n texlive-numericplots
Plotting numeric data is a task which has often to be done for
scientific papers. LaTeX itself provides no facilities for
drawing more than the simplest plots from supplied data. The
package will process user input, and uses PSTricks to plot the
results. The package provides Matlab functions to transform
Matlab results to plottable data.

%package -n texlive-numericplots-doc
Summary:        Documentation for numericplots
Version:        svn31729.2.0.2

Provides:       tex-numericplots-doc
AutoReqProv:    No

%description -n texlive-numericplots-doc
Documentation for numericplots

%package -n texlive-noconflict
Provides:       tex-noconflict = %{tl_version}
License:        LPPL 1.3
Summary:        Resolve macro name conflict between packages
Version:        svn30140.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(noconflict.sty) = %{tl_version}

%description -n texlive-noconflict
The package provides several commands to prefix (and hence
obscure) a macro's (or a sequence of macros') name, and to
restore the original macro(s) at places in a document where
they are needed.

%package -n texlive-noconflict-doc
Summary:        Documentation for noconflict
Version:        svn30140.1.0

Provides:       tex-noconflict-doc
AutoReqProv:    No

%description -n texlive-noconflict-doc
Documentation for noconflict

%package -n texlive-noindentafter
Provides:       tex-noindentafter = %{tl_version}
License:        LPPL 1.3
Summary:        Tool to prevent paragraph indentation after environments/macros
Version:        svn35709.0.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty)
Provides:       tex(noindentafter.sty) = %{tl_version}

%description -n texlive-noindentafter
The package, as the name suggests, supplies tools to
automatically suppress indentations in following paragraphs,
specifically those following a particular macro or environment.

%package -n texlive-noindentafter-doc
Summary:        Documentation for noindentafter
Version:        svn35709.0.2.2

Provides:       tex-noindentafter-doc
AutoReqProv:    No

%description -n texlive-noindentafter-doc
Documentation for noindentafter

%package -n texlive-noitcrul
Provides:       tex-noitcrul = %{tl_version}
License:        LPPL
Summary:        Improved underlines in mathematics
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(robustcommand.sty)
Provides:       tex(noitcrul.sty) = %{tl_version}

%description -n texlive-noitcrul
The package provides a (maths mode) \underline variant which
doesn't impose italics correction at the end.

%package -n texlive-noitcrul-doc
Summary:        Documentation for noitcrul
Version:        svn15878.0.2

Provides:       tex-noitcrul-doc
AutoReqProv:    No

%description -n texlive-noitcrul-doc
Documentation for noitcrul

%package -n texlive-nolbreaks
Provides:       tex-nolbreaks = %{tl_version}
License:        Public Domain
Summary:        No line breaks in text
Version:        svn26786.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nolbreaks.sty) = %{tl_version}

%description -n texlive-nolbreaks
Use \nolbreaks{some text} to prevent line breaks in "some
text". This has the advantage over \mbox{} that glue (rubber
space) remains flexible. Most common cases are handled here
(\linebreak is disabled, for example) but spaces hidden in
macros or { } can still create break-points.

%package -n texlive-nolbreaks-doc
Summary:        Documentation for nolbreaks
Version:        svn26786.1.2

Provides:       tex-nolbreaks-doc
AutoReqProv:    No

%description -n texlive-nolbreaks-doc
Documentation for nolbreaks

%package -n texlive-nomencl
Provides:       tex-nomencl = %{tl_version}
License:        LPPL
Summary:        Produce lists of symbols as in nomenclature
Version:        svn15878.3.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nomencl.sty) = %{tl_version}, tex(sample01.cfg) = %{tl_version}
Provides:       tex(sample02.cfg) = %{tl_version}, tex(sample04.cfg) = %{tl_version}
Provides:       tex(sample05.cfg) = %{tl_version}

%description -n texlive-nomencl
Produces lists of symbols using the capabilities of the
MakeIndex program.

%package -n texlive-nomencl-doc
Summary:        Documentation for nomencl
Version:        svn15878.3.1a

Provides:       tex-nomencl-doc
AutoReqProv:    No

%description -n texlive-nomencl-doc
Documentation for nomencl

%package -n texlive-nomentbl
Provides:       tex-nomentbl = %{tl_version}
License:        LPPL
Summary:        Nomenclature typeset in a longtable
Version:        svn16549.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(longtable.sty), tex(nomencl.sty), tex(ifthen.sty), tex(calc.sty)
Requires:       tex(array.sty)
Provides:       tex(nomentbl.sty) = %{tl_version}

%description -n texlive-nomentbl
Nomentbl typeset nomenclatures in a longtable instead of the
makeindex style of nomencl. A nomenclature entry may have three
arguments: Symbol, description and physical unit.

%package -n texlive-nomentbl-doc
Summary:        Documentation for nomentbl
Version:        svn16549.0.4

Provides:       tex-nomentbl-doc
AutoReqProv:    No

%description -n texlive-nomentbl-doc
Documentation for nomentbl

%package -n texlive-nonfloat
Provides:       tex-nonfloat = %{tl_version}
License:        Public Domain
Summary:        Non-floating table and figure captions
Version:        svn17598.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(nonfloat.sty) = %{tl_version}

%description -n texlive-nonfloat
Adjusts the figure and table environments to ensure that
centered objects as one line captions are centered as well.
Also the vertical spaces for table captions above the table are
changed.

%package -n texlive-nonfloat-doc
Summary:        Documentation for nonfloat
Version:        svn17598.1.0

Provides:       tex-nonfloat-doc
AutoReqProv:    No

%description -n texlive-nonfloat-doc
Documentation for nonfloat

%package -n texlive-nonumonpart
Provides:       tex-nonumonpart = %{tl_version}
License:        LPPL 1.2
Summary:        Prevent page numbers on part pages
Version:        svn22114.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nonumonpart.sty) = %{tl_version}

%description -n texlive-nonumonpart
The package bundles the answer to the long-standing FAQ about
removing page numbers on \part pages. The package accepts no
options and defines no user commands; the user needs only to
load it, and the requirement is met.

%package -n texlive-nonumonpart-doc
Summary:        Documentation for nonumonpart
Version:        svn22114.1

Provides:       tex-nonumonpart-doc
AutoReqProv:    No

%description -n texlive-nonumonpart-doc
Documentation for nonumonpart

%package -n texlive-nopageno
Provides:       tex-nopageno = %{tl_version}
License:        LPPL
Summary:        No page numbers in LaTeX documents
Version:        svn18128.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nopageno.sty) = %{tl_version}

%description -n texlive-nopageno
LaTeX's standard styles use two page styles, one on normal
pages and one on 'opening' pages with \maketitle or \chapter,
etc. Unfortunately there is only easy access to changing one of
these two so if you want something other than 'plain' on the
opening pages you must use \thispagestyle on each such page.
The fancyhdr package does provide a more flexible interface,
but if you just want an empty page style on all pages then this
package will do the job.

%package -n texlive-nopageno-doc
Summary:        Documentation for nopageno
Version:        svn18128.0

Provides:       tex-nopageno-doc
AutoReqProv:    No

%description -n texlive-nopageno-doc
Documentation for nopageno

%package -n texlive-notes
Provides:       tex-notes = %{tl_version}
License:        LPPL
Summary:        Mark sections of a document
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphics.sty)
Provides:       tex(notes.sty) = %{tl_version}

%description -n texlive-notes
The package provides environments to highlight significant
portions of text within a document, by putting the text in a
box and adding an icon in the margin. (The icons are provided
as 'fig' sources, processable by xfig.)

%package -n texlive-notes-doc
Summary:        Documentation for notes
Version:        svn42428
Provides:       tex-notes-doc
AutoReqProv:    No

%description -n texlive-notes-doc
Documentation for notes

%package -n texlive-notoccite
Provides:       tex-notoccite = %{tl_version}
License:        Public Domain
Summary:        Prevent trouble from citations in table of contents, etc
Version:        svn18129.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(notoccite.sty) = %{tl_version}

%description -n texlive-notoccite
If you have \cite commands in \section-like commands, or in
\caption, the citation will also appear in the table of
contents, or list of whatever. If you are also using an unsrt-
like bibliography style, these citations will come at the very
start of the bibliography, which is confusing. This package
suppresses the effect.

%package -n texlive-notoccite-doc
Summary:        Documentation for notoccite
Version:        svn18129.0

Provides:       tex-notoccite-doc
AutoReqProv:    No

%description -n texlive-notoccite-doc
Documentation for notoccite

%package -n texlive-nowidow
Provides:       tex-nowidow = %{tl_version}
License:        LPPL 1.3
Summary:        Avoid widows
Version:        svn24066.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty)
Provides:       tex(nowidow.sty) = %{tl_version}

%description -n texlive-nowidow
This package provides a useful macro to manage widow lines.

%package -n texlive-nowidow-doc
Summary:        Documentation for nowidow
Version:        svn24066.1.0

Provides:       tex-nowidow-doc
AutoReqProv:    No

%description -n texlive-nowidow-doc
Documentation for nowidow

%package -n texlive-nox
Provides:       tex-nox = %{tl_version}
License:        LPPL
Summary:        Adaptable tables
Version:        svn30991.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(longtable.sty)
Provides:       tex(nox.sty) = %{tl_version}

%description -n texlive-nox
The package allows data, text (including (La)TeX commands or
environments) to be formatted into a array which may be split.

%package -n texlive-nox-doc
Summary:        Documentation for nox
Version:        svn30991.1.0

Provides:       tex-nox-doc
AutoReqProv:    No

%description -n texlive-nox-doc
Documentation for nox

%package -n texlive-ntheorem
Provides:       tex-ntheorem = %{tl_version}
License:        LPPL
Summary:        Enhanced theorem environment
Version:        svn27609.1.33

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(ntheorem.sty) = %{tl_version}

%description -n texlive-ntheorem
The package offers enhancements for theorem-like environments:
easier control of layout; proper placement of endmarks even
when the environment ends with \end{enumerate} or
\end{displaymath} (including support for amsmath displayed-
equation environments); and support for making a list of
theorems, analagous to \listoffigures.

%package -n texlive-ntheorem-doc
Summary:        Documentation for ntheorem
Version:        svn27609.1.33

Provides:       tex-ntheorem-doc
AutoReqProv:    No

%description -n texlive-ntheorem-doc
Documentation for ntheorem

%package -n texlive-numberedblock
Provides:       tex-numberedblock = %{tl_version}
License:        LPPL 1.3
Summary:        Print a block of code, with unique index number
Version:        svn33109.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(numberedblock.sty) = %{tl_version}

%description -n texlive-numberedblock
The package has been created for the convenience of the report
writer; it provides the means to number, and label, code-block
snippets in your document. In this way, you can (unambiguously)
refer to each snippet elsewhere in your document.

%package -n texlive-numberedblock-doc
Summary:        Documentation for numberedblock
Version:        svn33109.1.10

Provides:       tex-numberedblock-doc
AutoReqProv:    No

%description -n texlive-numberedblock-doc
Documentation for numberedblock

%package -n texlive-numname
Provides:       tex-numname = %{tl_version}
License:        LPPL
Summary:        Convert a number to its English expression
Version:        svn18130.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(numname.sty) = %{tl_version}

%description -n texlive-numname
The package can generate cardinal (one, two, ...) and ordinal
(first, second, ...) numbers. The code derives from the memoir
class, and is extracted for the convenience of non-users of
that class.

%package -n texlive-numname-doc
Summary:        Documentation for numname
Version:        svn18130.0

Provides:       tex-numname-doc
AutoReqProv:    No

%description -n texlive-numname-doc
Documentation for numname

%package -n texlive-numprint
Provides:       tex-numprint = %{tl_version}
License:        LPPL
Summary:        Print numbers with separators and exponent if necessary
Version:        svn27498.1.39

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(array.sty), tex(calc.sty)
Provides:       tex(nbaseprt.sty) = %{tl_version}, tex(numprint.sty) = %{tl_version}
Provides:       tex(numprint032.sty) = %{tl_version}

%description -n texlive-numprint
The package numprint prints numbers with a separator every
three digits and converts numbers given as 12345.6e789 to
12\,345,6\cdot 10^{789}. Numbers are printed in the current
mode (text or math) in order to use the correct font. Many
things, including the decimal sign, the thousand separator, as
well as the product sign can be changed by the user, e.g., to
reach 12,345.6\times 10^{789}. If an optional argument is given
it is printed upright as unit. Numbers can be rounded to a
given number of digits. The package supports an automatic,
language-dependent change of the number format. Tabular
alignment using the tabular(*), array, tabularx, and longtable
environments (similar to the dcolumn and rccol packages) is
supported using all features of numprint. Additional text can
be added before and after the formatted number.

%package -n texlive-numprint-doc
Summary:        Documentation for numprint
Version:        svn27498.1.39

Provides:       tex-numprint-doc
AutoReqProv:    No

%description -n texlive-numprint-doc
Documentation for numprint

%package -n texlive-ocg-p
Provides:       tex-ocg-p = %{tl_version}
License:        LPPL
Summary:        PDF OCG support in LaTeX
Version:        svn28803.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(eso-pic.sty), tex(ifpdf.sty), tex(ifxetex.sty), tex(xkeyval.sty)
Requires:       tex(datatool.sty), tex(tikz.sty), tex(listings.sty)
Provides:       tex(ocg-p.sty) = %{tl_version}

%description -n texlive-ocg-p
The package provides OCG (Optional Content Groups) support
within a PDF document, replacing the ocg.sty distributed with
asymptote. Nested OCGs are supported. The package may be used
with PDFLatex and XeLaTeX.

%package -n texlive-ocg-p-doc
Summary:        Documentation for ocg-p
Version:        svn28803.0.4

Provides:       tex-ocg-p-doc
AutoReqProv:    No

%description -n texlive-ocg-p-doc
Documentation for ocg-p

%package -n texlive-ocgx
Provides:       tex-ocgx = %{tl_version}
License:        LPPL
Summary:        Use OCGs within a PDF document without JavaScript
Version:        svn28492.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ocg-p.sty)
Provides:       tex(ocgx.sty) = %{tl_version}, tex(tikzlibraryocgx.code.tex) = %{tl_version}

%description -n texlive-ocgx
The package extends the ocg package, which allows you to create
OCGs (Optional Content Groups) in PDF documents. (The ocg
package is distributed as part of Asymptote.) Every OCG
includes TeX material into a layer of the PDF file. Each of
these layers can be displayed or not. Links can enable or
disable the display of OCGs. The ocgx package does not use
Javascript embedded in the PDF document to enable (to show) or
disable (to hide) OCGs.

%package -n texlive-ocgx-doc
Summary:        Documentation for ocgx
Version:        svn28492.0.5

Provides:       tex-ocgx-doc
AutoReqProv:    No

%description -n texlive-ocgx-doc
Documentation for ocgx

%package -n texlive-ocgx2
Provides:       tex-ocgx2 = %{tl_version}
License:        LPPL 1.3
Summary:        Drop-in replacement for the 'ocgx' package; adds support for dvips+ps2pdf, XeLaTeX, dvipdfmx
Version:        svn48103
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xparse.sty), tex(atenddvi.sty), tex(ifpdf.sty), tex(l3keys2e.sty)
Requires:       tex(media9.sty), tex(tikz.sty)
Provides:       tex(fixocgx.sty) = %{tl_version}, tex(ocgx2.sty) = %{tl_version}

%description -n texlive-ocgx2
This package is a drop-in replacement for the ocgx package by
Paul Gaborit. It re-implements the functionality of the ocg,
ocgx, and ocg-p packages and adds support for all known engines
and back-ends including: LaTeX -> dvips -> ps2pdf/Distiller
(Xe)LaTeX(x) -> dvipdfmx PdfLaTeX and LuaLaTeX . It also
ensures compatibility with the media9 and animate packages.

%package -n texlive-ocgx2-doc
Summary:        Documentation for ocgx2
Version:        svn48103
Provides:       tex-ocgx2-doc
AutoReqProv:    No

%description -n texlive-ocgx2-doc
Documentation for ocgx2

%package -n texlive-ocr-latex
Provides:       tex-ocr-latex = %{tl_version}
License:        GPL+
Summary:        LaTeX support for ocr fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(ocr.sty) = %{tl_version}, tex(ot1oca.fd) = %{tl_version}
Provides:       tex(ot1ocra.fd) = %{tl_version}, tex(ot1ocrb.fd) = %{tl_version}
Provides:       tex(ot1ocrbn.fd) = %{tl_version}, tex(ot1ocrbns.fd) = %{tl_version}
Provides:       tex(ot1ocrbo.fd) = %{tl_version}, tex(ot1ocrbs.fd) = %{tl_version}

%description -n texlive-ocr-latex
The package supports use of both ocr-a and ocr-b fonts in LaTeX
documents.

%package -n texlive-ocr-latex-doc
Summary:        Documentation for ocr-latex
Version:        svn15878.0

Provides:       tex-ocr-latex-doc
AutoReqProv:    No

%description -n texlive-ocr-latex-doc
Documentation for ocr-latex

%package -n texlive-octavo
Provides:       tex-octavo = %{tl_version}
License:        LPPL
Summary:        Typeset books following classical design and layout
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(oct10.clo) = %{tl_version}, tex(oct11.clo) = %{tl_version}
Provides:       tex(oct12.clo) = %{tl_version}, tex(octavo.cls) = %{tl_version}

%description -n texlive-octavo
The octavo class is a modification of the standard LaTeX book
class. Its purpose is to typeset books following classical
design and layout principles, with the express intention of
encouraging the making of beautiful books by anyone with access
to a good printer and with an inclination towards venerable
crafts, e.g., bookbinding. The octavo class differs from the
book class by implementing many of the proposals and insights
of respected experts, especially Jan Tschichold and Hugh
Williamson. The documentation discusses methods to organise and
print out any text into signatures, which can then be gathered,
folded and sewn into a book.

%package -n texlive-octavo-doc
Summary:        Documentation for octavo
Version:        svn15878.1.2

Provides:       tex-octavo-doc
AutoReqProv:    No

%description -n texlive-octavo-doc
Documentation for octavo

%package -n texlive-oldstyle
Provides:       tex-oldstyle = %{tl_version}
License:        LPPL
Summary:        Old style numbers in OT1 encoding
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Ucmm.fd) = %{tl_version}, tex(oldstyle.sty) = %{tl_version}

%description -n texlive-oldstyle
Font information needed to load the cmmi and cmmib fonts for
use to produce oldstyle numbers.

%package -n texlive-oldstyle-doc
Summary:        Documentation for oldstyle
Version:        svn15878.0.2

Provides:       tex-oldstyle-doc
AutoReqProv:    No

%description -n texlive-oldstyle-doc
Documentation for oldstyle

%package -n texlive-omega
Provides:       tex-omega = %{tl_version}
License:        GPL+
Summary:        A wide-character-set extension of TeX
Version:        svn33046.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(omega.cfg) = %{tl_version}, tex(omega.map) = %{tl_version}
Provides:       tex(omding.tfm) = %{tl_version}, tex(omsea1.tfm) = %{tl_version}
Provides:       tex(omsea1b.tfm) = %{tl_version}, tex(omsea2.tfm) = %{tl_version}
Provides:       tex(omsea2b.tfm) = %{tl_version}, tex(omsea3.tfm) = %{tl_version}
Provides:       tex(omsea3b.tfm) = %{tl_version}, tex(omseco.tfm) = %{tl_version}
Provides:       tex(omsecob.tfm) = %{tl_version}, tex(omsecobi.tfm) = %{tl_version}
Provides:       tex(omsecoi.tfm) = %{tl_version}, tex(omsecx.tfm) = %{tl_version}
Provides:       tex(omsecy.tfm) = %{tl_version}, tex(omsegr.tfm) = %{tl_version}
Provides:       tex(omsegrb.tfm) = %{tl_version}, tex(omsegrbi.tfm) = %{tl_version}
Provides:       tex(omsegri.tfm) = %{tl_version}, tex(omseha.tfm) = %{tl_version}
Provides:       tex(omseip.tfm) = %{tl_version}, tex(omsela.tfm) = %{tl_version}
Provides:       tex(omselab.tfm) = %{tl_version}, tex(omselabi.tfm) = %{tl_version}
Provides:       tex(omselai.tfm) = %{tl_version}, tex(omseti.tfm) = %{tl_version}
Provides:       tex(omssti.tfm) = %{tl_version}, tex(omding.pfb) = %{tl_version}
Provides:       tex(omsea1.pfb) = %{tl_version}, tex(omsea1b.pfb) = %{tl_version}
Provides:       tex(omsea2.pfb) = %{tl_version}, tex(omsea2b.pfb) = %{tl_version}
Provides:       tex(omsea3.pfb) = %{tl_version}, tex(omsea3b.pfb) = %{tl_version}
Provides:       tex(omseco.pfb) = %{tl_version}, tex(omsecob.pfb) = %{tl_version}
Provides:       tex(omsecobi.pfb) = %{tl_version}, tex(omsecoi.pfb) = %{tl_version}
Provides:       tex(omsecx.pfb) = %{tl_version}, tex(omsecy.pfb) = %{tl_version}
Provides:       tex(omsecyb.pfb) = %{tl_version}, tex(omsecyi.pfb) = %{tl_version}
Provides:       tex(omsegr.pfb) = %{tl_version}, tex(omsegrb.pfb) = %{tl_version}
Provides:       tex(omsegrbi.pfb) = %{tl_version}, tex(omsegri.pfb) = %{tl_version}
Provides:       tex(omseha.pfb) = %{tl_version}, tex(omsehe.pfb) = %{tl_version}
Provides:       tex(omseip.pfb) = %{tl_version}, tex(omsela.pfb) = %{tl_version}
Provides:       tex(omselab.pfb) = %{tl_version}, tex(omselabi.pfb) = %{tl_version}
Provides:       tex(omselai.pfb) = %{tl_version}, tex(omseti.pfb) = %{tl_version}
Provides:       tex(omssti.pfb) = %{tl_version}, tex(bghyph.tex) = %{tl_version}
Provides:       tex(lthyph.tex) = %{tl_version}, tex(srhyph.tex) = %{tl_version}
Provides:       tex(grlccode.tex) = %{tl_version}, tex(omega.tex) = %{tl_version}

%description -n texlive-omega
A development of TeX, which deals in multi-octet Unicode
characters, to enable native treatment of a wide range of
languages without changing character-set. Work on Omega seems
to have ceased: its immediate successor was to be the aleph
project (though that too has stalled). Projects developing
Omega (and Aleph) ideas include Omega-2 and LuaTeX.

%package -n texlive-omega-doc
Summary:        Documentation for omega
Version:        svn33046.0

Provides:       tex-omega-doc
AutoReqProv:    No

%description -n texlive-omega-doc
Documentation for omega

%package -n texlive-onlyamsmath
Provides:       tex-onlyamsmath = %{tl_version}
License:        LPPL
Summary:        Inhibit use of non-amsmath mathematics markup when using amsmath
Version:        svn42927
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amsmath.sty)
Provides:       tex(onlyamsmath.sty) = %{tl_version}

%description -n texlive-onlyamsmath
This package inhibits the usage of plain TeX and (on demand) of
standard LaTeX mathematics environments. This is useful for
class writers who want to encourage their users to use the
environments provided by the amsmath package.

%package -n texlive-onlyamsmath-doc
Summary:        Documentation for onlyamsmath
Version:        svn42927
Provides:       tex-onlyamsmath-doc
AutoReqProv:    No

%description -n texlive-onlyamsmath-doc
Documentation for onlyamsmath

%package -n texlive-opcit
Provides:       tex-opcit = %{tl_version}
License:        LPPL
Summary:        Footnote-style bibliographical references
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(hyperref.sty)
Provides:       tex(opcit.sty) = %{tl_version}

%description -n texlive-opcit
This package addresses the problem of expressing citations in a
style that is natural for humanities studies, yet does not
interfere with the flow of text (as author-year styles do). The
package differs from footbib in that it uses real footnotes,
potentially in the same series as any of the document's other
footnotes. Opcit also, as its name implies, avoids repetition
of full citations, achieving this, to a large extent,
automatically.

%package -n texlive-opcit-doc
Summary:        Documentation for opcit
Version:        svn15878.1.1

Provides:       tex-opcit-doc
AutoReqProv:    No

%description -n texlive-opcit-doc
Documentation for opcit

%package -n texlive-optional
Provides:       tex-optional = %{tl_version}
License:        LPPL
Summary:        Facilitate optional printing of parts of a document
Version:        svn18131.2.2b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(optional.sty) = %{tl_version}

%description -n texlive-optional
Optional provides simple, flexible, optional compilation of
LaTeX documents. Option switches may be given via package
options, by the \UseOption command, or interactively via the
\AskOption command (help text may be provided, by defining the
\ExplainOptions command). The package is not robust, in the way
that comment package is, against ill-behaved text. In
particular, verbatim text may not be directly included in
optional sections (whether they're included or not).

%package -n texlive-optional-doc
Summary:        Documentation for optional
Version:        svn18131.2.2b

Provides:       tex-optional-doc
AutoReqProv:    No

%description -n texlive-optional-doc
Documentation for optional

%package -n texlive-otibet
Provides:       tex-otibet = %{tl_version}
License:        LPPL
Summary:        otibet package
Version:        svn45777
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(tibetan.tfm) = %{tl_version}, tex(ot1tib.fd) = %{tl_version}
Provides:       tex(otibet.sty) = %{tl_version}, tex(otibet.tex) = %{tl_version}
Provides:       tex(t1tib.fd) = %{tl_version}

%description -n texlive-otibet
otibet package

%package -n texlive-otibet-doc
Summary:        Documentation for otibet
Version:        svn45777
Provides:       tex-otibet-doc
AutoReqProv:    No

%description -n texlive-otibet-doc
Documentation for otibet

%package -n texlive-outline
Provides:       tex-outline = %{tl_version}
License:        LPPL
Summary:        List environment for making outlines
Version:        svn18360.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(outline.sty) = %{tl_version}

%description -n texlive-outline
The package defines an outline environment, which provides
facilities similar to enumerate, but up to 6 levels deep.

%package -n texlive-outline-doc
Summary:        Documentation for outline
Version:        svn18360.0

Provides:       tex-outline-doc
AutoReqProv:    No

%description -n texlive-outline-doc
Documentation for outline

%package -n texlive-outliner
Provides:       tex-outliner = %{tl_version}
License:        GPL+
Summary:        Change section levels easily
Version:        svn21095.0.94

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(outliner.sty) = %{tl_version}

%description -n texlive-outliner
Allows you to write "\Level 2 {Some heading}" instead of the
usual \section stuff; the definitions of the levels can then
easily be changed. There is a mechanism for shifting all
levels. This makes it easy to bundle existing articles into a
compilation.

%package -n texlive-outliner-doc
Summary:        Documentation for outliner
Version:        svn21095.0.94

Provides:       tex-outliner-doc
AutoReqProv:    No

%description -n texlive-outliner-doc
Documentation for outliner

%package -n texlive-outlines
Provides:       tex-outlines = %{tl_version}
License:        LPPL
Summary:        Produce "outline" lists
Version:        svn25192.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(outlines.sty) = %{tl_version}

%description -n texlive-outlines
Defines an outline environment, which allows outline-style
indented lists with freely mixed levels up to four levels deep.
It replaces the nested begin/end pairs by different item tags
\1 to \4 for each nesting level. This is very convenient in
cases where nested lists are used a lot, such as for to-do
lists or presentation slides.

%package -n texlive-outlines-doc
Summary:        Documentation for outlines
Version:        svn25192.1.1

Provides:       tex-outlines-doc
AutoReqProv:    No

%description -n texlive-outlines-doc
Documentation for outlines

%package -n texlive-overpic
Provides:       tex-overpic = %{tl_version}
License:        LPPL
Summary:        Combine LaTeX commands over included graphics
Version:        svn45500
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(epic.sty)
Provides:       tex(overpic.sty) = %{tl_version}

%description -n texlive-overpic
The overpic environment is a cross between the LaTeX picture
environment and the \includegraphics command of graphicx. The
resulting picture environment has the same dimensions as the
included graphic. LaTeX commands can be placed on the graphic
at defined positions; a grid for orientation is available.

%package -n texlive-overpic-doc
Summary:        Documentation for overpic
Version:        svn45500
Provides:       tex-overpic-doc
AutoReqProv:    No

%description -n texlive-overpic-doc
Documentation for overpic

%package -n texlive-odsfile
Provides:       tex-odsfile = %{tl_version}
License:        LPPL 1.3
Summary:        Read OpenDocument Spreadsheet documents as LaTeX tables
Version:        svn38449

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(luacode.sty), tex(xkeyval.sty)
Provides:       tex(odsfile.sty) = %{tl_version}

%description -n texlive-odsfile
The distribution includes a package and a lua library that can
together read OpenDocument spreadsheet documents as LaTeX
tables. Cells in the tables may be processed by LaTeX macros,
so that (for example) the package may be used for drawing some
plots. The package uses lua's zip library.

%package -n texlive-odsfile-doc
Summary:        Documentation for odsfile
Version:        svn38449

Provides:       tex-odsfile-doc
AutoReqProv:    No

%description -n texlive-odsfile-doc
Documentation for odsfile

%package -n texlive-ot-tableau
Provides:       tex-ot-tableau = %{tl_version}
License:        LPPL
Summary:        Optimality Theory tableaux in LaTeX
Version:        svn44889
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xstring.sty), tex(amssymb.sty), tex(bbding.sty), tex(suffix.sty)
Requires:       tex(colortbl.sty), tex(arydshln.sty), tex(rotating.sty), tex(tipa.sty)
Provides:       tex(ot-tableau.sty) = %{tl_version}

%description -n texlive-ot-tableau
The package makes it easy to create beautiful optimality-
theoretic tableaux. The LaTeX source is visually very similar
to a formatted tableau, which makes working with the source
code painless (well, less painful). A variety of stylistic
variants are available to suit personal taste.

%package -n texlive-ot-tableau-doc
Summary:        Documentation for ot-tableau
Version:        svn44889
Provides:       tex-ot-tableau-doc
AutoReqProv:    No

%description -n texlive-ot-tableau-doc
Documentation for ot-tableau

%package -n texlive-oubraces
Provides:       tex-oubraces = %{tl_version}
License:        Copyright only
Summary:        Braces over and under a formula
Version:        svn21833.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(oubraces.sty) = %{tl_version}

%description -n texlive-oubraces
Provides a means to interleave \overbrace and \underbrace in
the same formula.

%package -n texlive-oubraces-doc
Summary:        Documentation for oubraces
Version:        svn21833.0

Provides:       tex-oubraces-doc
AutoReqProv:    No

%description -n texlive-oubraces-doc
Documentation for oubraces

%package -n texlive-nostarch
Provides:       tex-nostarch = %{tl_version}
License:        LPPL
Summary:        LaTeX class for No Starch Press
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(fancyhdr.sty), tex(fancyvrb.sty), tex(booktabs.sty)
Requires:       tex(graphicx.sty), tex(listings.sty), tex(caption.sty), tex(makeidx.sty)
Requires:       tex(upquote.sty), tex(ragged2e.sty), tex(hyperref.sty)
Provides:       tex(nostarch.cls) = %{tl_version}, tex(nshyper.sty) = %{tl_version}

%description -n texlive-nostarch
The package provides the "official" LaTeX style for No Starch
Press. Provided are a class, a package for interfacing to
hyperref and an index style file. The style serves both for
printed and for electronic books.

%package -n texlive-nostarch-doc
Summary:        Documentation for nostarch
Version:        svn15878.1.3

Provides:       tex-nostarch-doc
AutoReqProv:    No

%description -n texlive-nostarch-doc
Documentation for nostarch

%package -n texlive-nrc
Provides:       tex-nrc = %{tl_version}
License:        LPPL
Summary:        Class for the NRC technical journals
Version:        svn29027.2.01a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(multicol.sty)
Provides:       tex(nrc1.cls) = %{tl_version}, tex(nrc1.sty) = %{tl_version}
Provides:       tex(nrc2.cls) = %{tl_version}, tex(nrc2.sty) = %{tl_version}

%description -n texlive-nrc
Macros, and some documentation, for typesetting papers for
submission to journals published by the National Research
Council Research Press. At present, only nrc2.cls (for two-
column layout) should be used.

%package -n texlive-nrc-doc
Summary:        Documentation for nrc
Version:        svn29027.2.01a

Provides:       tex-nrc-doc
AutoReqProv:    No

%description -n texlive-nrc-doc
Documentation for nrc

%package -n texlive-onrannual
Provides:       tex-onrannual = %{tl_version}
License:        LPPL 1.3
Summary:        Class for Office of Naval Research Ocean Battlespace Sensing annual report
Version:        svn17474.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(mathptmx.sty), tex(geometry.sty), tex(authblk.sty), tex(parskip.sty)
Requires:       tex(caption.sty), tex(hyperref.sty)
Provides:       tex(onrannual.cls) = %{tl_version}

%description -n texlive-onrannual
This is an unofficial document class for writing ONR annual
reports using LaTeX; as ONR has had numerous problems with
LaTeX-generated PDF submissions in the past. A skeleton
document (and its PDF output) are included.

%package -n texlive-onrannual-doc
Summary:        Documentation for onrannual
Version:        svn17474.1.1

Provides:       tex-onrannual-doc
AutoReqProv:    No

%description -n texlive-onrannual-doc
Documentation for onrannual

%package -n texlive-opteng
Provides:       tex-opteng = %{tl_version}
License:        LPPL
Summary:        SPIE Optical Engineering and OE Letters manuscript template
Version:        svn27331.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(opteng.sty) = %{tl_version}

%description -n texlive-opteng
With this template, and associated style and LaTeX packages, it
is possible to estimate the page length of manuscripts for
submission to the SPIE journals 'Optical Engineering' and
'Optical Engineering Letters'. With a strict three-page limit,
this is particularly important for the latter. The template
gives simple instructions on how to prepare the manuscript.

%package -n texlive-opteng-doc
Summary:        Documentation for opteng
Version:        svn27331.1.0

Provides:       tex-opteng-doc
AutoReqProv:    No

%description -n texlive-opteng-doc
Documentation for opteng

%package -n texlive-nuc
Provides:       tex-nuc = %{tl_version}
License:        LPPL
Summary:        Notation for nuclear isotopes
Version:        svn22256.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(nuc.sty) = %{tl_version}

%description -n texlive-nuc
A simple package providing nuclear sub- and superscripts as
commonly used in radiochemistry, radiation science, and nuclear
physics and engineering applications. Isotopes which have Z
with more digits than A require special spacing to appear
properly; this spacing is supported in the package.

%package -n texlive-nuc-doc
Summary:        Documentation for nuc
Version:        svn22256.0.1

Provides:       tex-nuc-doc
AutoReqProv:    No

%description -n texlive-nuc-doc
Documentation for nuc

%package -n texlive-objectz
Provides:       tex-objectz = %{tl_version}
License:        LPPL
Summary:        Macros for typesetting Object Z
Version:        svn19389.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(oz.sty) = %{tl_version}

%description -n texlive-objectz
The package will typeset both Z and Object-Z specifications; it
develops the original zed package

%package -n texlive-objectz-doc
Summary:        Documentation for objectz
Version:        svn19389.0

Provides:       tex-objectz-doc
AutoReqProv:    No

%description -n texlive-objectz-doc
Documentation for objectz

%package -n texlive-normalcolor-doc
Provides:       tex-normalcolor-doc = %{tl_version}
License:        LPPL
Summary:        doc files of normalcolor
Version:        svn40125

AutoReqProv:    No

%description -n texlive-normalcolor-doc
Documentation for normalcolor

%package -n texlive-normalcolor
Provides:       tex-normalcolor = %{tl_version}
License:        LPPL
Summary:        Changing \normalcolor
Version:        svn40125

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(normalcolor.sty) = %{tl_version}

%description -n texlive-normalcolor
This package provides a command \setnormalcolor with the same
syntax as the command \color either of package color or of
package xcolor. However, \setnormalcolor will not change the
current colour but the normal / default color.

%package -n texlive-noto-doc
Provides:       tex-noto-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of noto
Version:        svn46687
AutoReqProv:    No

%description -n texlive-noto-doc
Documentation for noto

%package -n texlive-noto
Provides:       tex-noto = %{tl_version}
License:        LPPL and OFL
Summary:        Support for Noto fonts
Version:        svn46687
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(noto.sty) = %{tl_version}, tex(noto.map) = %{tl_version}
Provides:       tex(OT1NotoSans-TLF.fd) = %{tl_version}, tex(TS1NotoSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1NotoSerif-TLF.fd) = %{tl_version}
Provides:       tex(LY1NotoSans-TLF.fd) = %{tl_version}, tex(OT1NotoSerif-TLF.fd) = %{tl_version}
Provides:       tex(T1NotoSerif-TLF.fd) = %{tl_version}, tex(T1NotoSans-TLF.fd) = %{tl_version}
Provides:       tex(LY1NotoSerif-TLF.fd) = %{tl_version}
Provides:       tex(NotoSerif-Regular.pfb) = %{tl_version}
Provides:       tex(NotoSerif-Italic.pfb) = %{tl_version}
Provides:       tex(NotoSans-Regular.pfb) = %{tl_version}
Provides:       tex(NotoSerif-Bold.pfb) = %{tl_version}, tex(NotoSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(NotoSans-Italic.pfb) = %{tl_version}
Provides:       tex(NotoSans-Bold.pfb) = %{tl_version}, tex(NotoSerif-BoldItalic.pfb) = %{tl_version}
Provides:       tex(nto_5drdqr.enc) = %{tl_version}, tex(nto_rq4ual.enc) = %{tl_version}
Provides:       tex(nto_m46tqg.enc) = %{tl_version}, tex(nto_5ritkc.enc) = %{tl_version}
Provides:       tex(NotoSans-Italic.otf) = %{tl_version}
Provides:       tex(NotoSerif-Regular.otf) = %{tl_version}
Provides:       tex(NotoSans-Bold.otf) = %{tl_version}, tex(NotoSerif-BoldItalic.otf) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic.otf) = %{tl_version}
Provides:       tex(NotoSerif-Italic.otf) = %{tl_version}
Provides:       tex(NotoSerif-Bold.otf) = %{tl_version}, tex(NotoSans-Regular.otf) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSans-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSans-tlf-t1.vf) = %{tl_version}, tex(NotoSans-Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSerif-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSans-tlf-ot1.vf) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(NotoSans-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ly1.vf) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSerif-tlf-t1.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSans-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(NotoSerif-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(NotoSans-Italic-tlf-ly1--base.tfm) = %{tl_version}

%description -n texlive-noto
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the NotoSerif and NotoSans families of fonts,
designed by Steve Matteson for Google.

%package -n texlive-nucleardata-doc
Provides:       tex-nucleardata-doc = %{tl_version}
License:        LPPL
Summary:        doc files of nucleardata
Version:        svn47307
AutoReqProv:    No

%description -n texlive-nucleardata-doc
Documentation for nucleardata

%package -n texlive-nucleardata
Provides:       tex-nucleardata = %{tl_version}
License:        LPPL
Summary:        Provides data about atomic nuclides for documents
Version:        svn47307
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(nucleardata.sty) = %{tl_version}

%description -n texlive-nucleardata
The package provides data and commands for including nuclear
and atomic mass and energy data in LaTeX documents. It uses the
PythonTeX package and requires pythontex.exe to be called with
the TeX file as the argument.

%package -n texlive-nwejm-doc
Provides:       tex-nwejm-doc = %{tl_version}
License:        LPPL
Summary:        doc files of nwejm
Version:        svn47411
AutoReqProv:    No

%description -n texlive-nwejm-doc
Documentation for nwejm

%package -n texlive-nwejm
Provides:       tex-nwejm = %{tl_version}
License:        LPPL
Summary:        Support for the journal "North-Western European Journal of Mathematics"
Version:        svn47411
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(nwejm.cls) = %{tl_version}, tex(nwejmart.cls) = %{tl_version}
Provides:       tex(nwejm.cfg) = %{tl_version}

%description -n texlive-nwejm
The bundle includes LaTeX classes and BibLaTeX styles files
dedicated to the new journal "North-Western European Journal of
Mathematics".

%package -n texlive-optidef-doc
Provides:       tex-optidef-doc = %{tl_version}
License:        LPPL
Summary:        doc files of optidef
Version:        svn48228
AutoReqProv:    No

%description -n texlive-optidef-doc
Documentation for optidef

%package -n texlive-optidef
Provides:       tex-optidef = %{tl_version}
License:        LPPL
Summary:        Provides a standard set of environments for writing minimization problems
Version:        svn48228
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(optidef.sty) = %{tl_version}

%description -n texlive-optidef
This small library provides a standard set of environments for
writing minimization problems. It automatically aligns the
problems in three points with an optional fourth: Beginning of
the words "minimize/argmin" and "subject to" The objective
function and the longest left hand side of the constraints The
$= | > | <$ signs of the constraints. Optionally, the user can
add manually a double align character && to align some common
constraints feature. A clear example could be the constraints
names, e.g. (boundary constraint) alignment with (dynamic
constraint). Furthermore, it provides an easy interface to
define optimization problem for three different reference
situations: Where no equation is referenced/numbered. Where the
problem is referenced with a single number. Where each equation
has an individual reference. Finally, it also allows a
definition of any optimization problem without a limitless
number of constraints.

%package -n texlive-options-doc
Provides:       tex-options-doc = %{tl_version}
License:        LPPL
Summary:        doc files of options
Version:        svn39030

AutoReqProv:    No

%description -n texlive-options-doc
Documentation for options

%package -n texlive-options
Provides:       tex-options = %{tl_version}
License:        LPPL
Summary:        Provides convenient key-value options for LaTeX package writers
Version:        svn39030

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(options.sty) = %{tl_version}

%description -n texlive-options
The options package provides easy to use key-value options for
LaTeX package writers. It has a similar interface as pgfkeys
with path options but comes with more built-in data types and
more convenient support for families and searching.

%package -n texlive-obsolete
License:        Public Domain
Provides:       texlive-context-fixme = %{epoch}:svn29341.0.obsolete
Obsoletes:      texlive-context-fixme <= 6:svn29341.0
Provides:       texlive-context-games = %{epoch}:svn23167.0.obsolete
Obsoletes:      texlive-context-games <= 6:svn23167.0
Provides:       texlive-context-games-doc = %{epoch}:svn23167.0.obsolete
Obsoletes:      texlive-context-games-doc <= 6:svn23167.0
Provides:       texlive-context-lilypond = %{epoch}:svn23167.0.obsolete
Obsoletes:      texlive-context-lilypond <= 6:svn23167.0
Provides:       texlive-context-lilypond-doc = %{epoch}:svn23167.0.obsolete
Obsoletes:      texlive-context-lilypond-doc <= 6:svn23167.0
Provides:       texlive-knuthotherfonts = %{epoch}:svn13293.0.obsolete
Obsoletes:      texlive-knuthotherfonts <= 6:svn13293.0
Provides:       texlive-scheme-xml = %{epoch}:svn40631.obsolete
Obsoletes:      texlive-scheme-xml <= 6:svn40631
Provides:       texlive-mil3-doc = %{epoch}:svn21677.0.obsolete
Obsoletes:      texlive-mil3-doc <= 6:svn21677.0
Provides:       texlive-pstricks-examples-en-doc = %{epoch}:svn29349.0.obsolete
Obsoletes:      texlive-pstricks-examples-en-doc <= 6:svn29349.0
Provides:       texlive-pstricks-examples-doc = %{epoch}:svn21511.0.obsolete
Obsoletes:      texlive-pstricks-examples-doc <= 6:svn21511.0
Provides:       texlive-voss-mathmode-doc = %{epoch}:svn36093.2.47.obsolete
Obsoletes:      texlive-voss-mathmode-doc <= 6:svn36093.2.47
Provides:       tex-japanese = %{epoch}:svn30855.1.3.obsolete
Provides:       texlive-japanese = %{epoch}:svn30855.1.3.obsolete
Obsoletes:      texlive-japanese <= 6:svn30855.1.3
Provides:       tex-japanese-doc = %{epoch}:svn30855.1.3.obsolete
Provides:       texlive-japanese-doc = %{epoch}:svn30855.1.3.obsolete
Obsoletes:      texlive-japanese-doc <= 6:svn30855.1.3
Provides:       texlive-getargs = %{epoch}:svn41415.obsolete
Obsoletes:      texlive-getargs <= 6:svn41415
Summary:        This package handles obsolete texlive subpackages

%description -n texlive-obsolete
This package is a metapackage which handles obsolete texlive subpackages.
It does not contain the contents of the packages that it obsoletes.

%package -n texlive-nodetree
Summary:        visualize node lists in a tree view
Version:        svn43011
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(nodetree.sty) = %{tl_version}, tex(nodetree.tex) = %{tl_version}

%description -n texlive-nodetree
nodetree is a development package that visualizes the structure
of node lists. nodetree shows its debug informations in the
console output when you compile a LuaTeX file. It uses a
similar visual representation for node lists as the UNIX tree
command for a folder structure.

%package -n texlive-notespages
Summary:        Filling documents with notes pages and notes areas
Version:        svn41906
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(notespages.sty) = %{tl_version}

%description -n texlive-notespages
This package package provides one macro to insert a single
notes page and another to fill the document with multiple notes
pages, until the total number of pages (so far) is a multiple
of a given number. A third command can be used to fill half
empty pages with a notes area.

%package -n texlive-notestex
Summary:        An all-in-one LaTeX notes package for students
Version:        svn45396
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(NotesTeX.sty) = %{tl_version}

%description -n texlive-notestex
This is a modification of the original Jhep journal format in
order to suit the needs of students in university. The goal of
this package was to make notetaking easier for students and
offer easy support for marginnotes along with a reliable and
legible formatting structure.

%package -n texlive-novel
Summary:        Class for printing fiction, such as novels
Version:        svn47492
License:        LPPL and OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(NovelDeco.otf) = %{tl_version}, tex(novel-CGATSTR001.clo) = %{tl_version}
Provides:       tex(novel-CalculateLayout.sty) = %{tl_version}
Provides:       tex(novel-ChapterScene.sty) = %{tl_version}
Provides:       tex(novel-FOGRA39.clo) = %{tl_version}, tex(novel-FileData.sty) = %{tl_version}
Provides:       tex(novel-FontDefaults.sty) = %{tl_version}
Provides:       tex(novel-Footnotes.sty) = %{tl_version}
Provides:       tex(novel-HeadFootStyles.sty) = %{tl_version}
Provides:       tex(novel-Images.sty) = %{tl_version}, tex(novel-JC200103.clo) = %{tl_version}
Provides:       tex(novel-LayoutSettings.sty) = %{tl_version}
Provides:       tex(novel-TextMacros.sty) = %{tl_version}
Provides:       tex(novel-glyphtounicode.tex) = %{tl_version}
Provides:       tex(novel-microtype.cfg) = %{tl_version}
Provides:       tex(novel-pdfx.sty) = %{tl_version}, tex(novel-xmppacket.sty) = %{tl_version}
Provides:       tex(novel.cls) = %{tl_version}

%description -n texlive-novel
This LuaLaTeX document class is specifically written to meet
the needs of original fiction writers, who are typesetting
their own novels for non-color print-on-demand technology.
Built-in PDF/X is available, using new technology. The package
is well suited for detective novels, science fiction, and short
stories. It is however not recommended for creating color
picture books or dissertations.

%package -n texlive-numnameru
Summary:        converts a number to the russian spelled out name
Version:        svn44895
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(numnameru.sty) = %{tl_version}

%description -n texlive-numnameru
This package converts a numerical number to the russian spelled
out name of the number. For example, 1 - odin, 2 - dva, 12 -
dvenadtsat'.

%package -n texlive-numspell
Summary:        Spelling cardinal and ordinal numbers
Version:        svn45441
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(numspell-english.sty) = %{tl_version}
Provides:       tex(numspell-french.sty) = %{tl_version}
Provides:       tex(numspell-german.sty) = %{tl_version}
Provides:       tex(numspell-italian.sty) = %{tl_version}
Provides:       tex(numspell-magyar.sty) = %{tl_version}
Provides:       tex(numspell.sty) = %{tl_version}

%description -n texlive-numspell
This package supports the spelling of cardinal and ordinal
numbers. Supported languages are English, French, German,
Hungarian, and Italian. The package requires xstring,
pdftexcmds, and etoolbox.

%package -n texlive-octave
Summary:        Typeset musical pitches with octave designations
Version:        svn45674
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(octave.sty) = %{tl_version}

%description -n texlive-octave
This package package typesets musical pitch names with
designation for the octave in either the Helmholtz system (with
octave numbers), or the traditional system (with prime
symbols). Authors can just write \pitch{C}{4} and the pitches
will be rendered correctly depending on which package option
was selected. The system can also be changed mid-document.

%package -n texlive-olsak-misc
Summary:        Collection with plain TeX macros written by Petr Olsak
Version:        svn41526
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(qrcode.tex) = %{tl_version}, tex(scanbase.tex) = %{tl_version}
Provides:       tex(scancsv.tex) = %{tl_version}, tex(xmlparser.tex) = %{tl_version}

%description -n texlive-olsak-misc
This is a collection with various single-file plain TeX macros
written by Petr Olsak. The documentation is included in each
file separately. booklet.tex: re-orders PDF pages and collects
them for booklet printing cnv.tex: conversion of texts
cnv-pu.tex: example of usage of cnv.tex --- pdf outlines in
Unicode cnv-word.tex: example of usage of cnv.tex --- word to
word conversion eparam.tex: Full expansion during parameter
scanning fun-coffee.tex: generates splotches in the document
openclose.tex: repairs balanced text between \Open ...\Close
pair qrcode.tex: QR code generated at TeX level scanbase.tex:
parser of text-style mysql outputs scancsv.tex: parser of CSV
format seplist.tex: macros with alternative separators of a
parameter xmlparser.tex: parser of XML language

%package -n texlive-notex-bst
Summary:        A BibTeX style that outputs HTML
Version:        svn42361
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(noTeX.bst) = %{tl_version}

%description -n texlive-notex-bst
noTeX.bst produces a number of beautifully formatted HTML P
elements instead of TeX code. It can be used to automatically
generate bibliographies to be served on the web starting from
BibTeX files.

%package -n texlive-onedown
Summary:        Typeset Bridge Diagrams
Version:        svn47828
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ODw-danish.trsl) = %{tl_version}, tex(ODw-dutch.trsl) = %{tl_version}
Provides:       tex(ODw-english.trsl) = %{tl_version}, tex(ODw-fallback.trsl) = %{tl_version}
Provides:       tex(ODw-french.trsl) = %{tl_version}, tex(ODw-german.trsl) = %{tl_version}
Provides:       tex(ODw-norwegian.trsl) = %{tl_version}, tex(ODw-swedish.trsl) = %{tl_version}
Provides:       tex(ODw-turkish.trsl) = %{tl_version}, tex(onedown.sty) = %{tl_version}

%description -n texlive-onedown
This is a comprehensive package to draw all sorts of bridge
diagrams, including hands (stand alone or arround a compass),
bidding tables (stand alone or in connection with
hands/compass), trick tables, and expert quizzes. Features:
Works for all fontsizes from \ssmall to \HUGE. Different fonts
for hands, bidding diagrams, compass, etc. are possible.
Annotations to card and bidding diagrams. Automated check on
consistency of suit and hands. Multilingual output of bridge
terms. Extensive documentation: User manual, Reference manual,
and Examples.

%package -n texlive-oplotsymbl
Summary:        Some symbols which are not easily available
Version:        svn44951
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(tikz.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(oplotsymbl.sty) = %{tl_version}

%description -n texlive-oplotsymbl
This package is named oPlotSymbl and it includes symbols, which
longdesc are not easily available. Especially, these symbols are used in
longdesc scientific plots, but the potential user is allowed to use them
longdesc in other ways. This package uses TikZ and xcolor.

%package -n texlive-outlining
Summary:        Create outlines for scientific documents
Version:        svn45601
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(outlining.sty) = %{tl_version}

%description -n texlive-outlining
Every scientific document requires outlining before it is
written. This package adds simple macros for your LaTeX
document.

%package -n texlive-overlays
Summary:        Incremental slides
Version:        svn46122
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(xcolor.sty)
Requires:       tex(environ.sty), tex(pgffor.sty)
Provides:       tex(overlays.sty) = %{tl_version}

%description -n texlive-overlays
The overlay package allows to write presentations with
incremental slides. It does not presuppose any specific
document class. Rather, it is a lightweight alternative to
full-fledged presentation classes like beamer. The package
requires xcolor, environ, and pgffor (from the pgf bundle).

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x


cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/newpx public/ocr-b-outline"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/fonts/type1/public/oldstandard/*
rm -f %{buildroot}%{_datadir}/fonts/newpx
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-omega
%license gpl.txt
%{_texdir}/texmf-dist/dvips/omega/
%{_texdir}/texmf-dist/fonts/afm/public/omega/
%{_texdir}/texmf-dist/fonts/map/dvips/omega/
%{_texdir}/texmf-dist/fonts/ofm/public/omega/
%{_texdir}/texmf-dist/fonts/ovf/public/omega/
%{_texdir}/texmf-dist/fonts/ovp/public/omega/
%{_texdir}/texmf-dist/fonts/tfm/public/omega/
%{_texdir}/texmf-dist/fonts/type1/public/omega/
%{_texdir}/texmf-dist/omega/ocp/
%{_texdir}/texmf-dist/omega/otp/
%{_texdir}/texmf-dist/tex/generic/encodings/
%{_texdir}/texmf-dist/tex/generic/omegahyph/
%{_texdir}/texmf-dist/tex/plain/omega/

%files -n texlive-omega-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/omega/base/

%files -n texlive-norasi-c90
%{_texdir}/texmf-dist/dvips/norasi-c90/
%{_texdir}/texmf-dist/fonts/map/dvips/norasi-c90/
%{_texdir}/texmf-dist/fonts/tfm/public/norasi-c90/

%files -n texlive-notes2bib
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/notes2bib/

%files -n texlive-notes2bib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/notes2bib/

%files -n texlive-ordinalpt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ordinalpt/

%files -n texlive-ordinalpt-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ordinalpt/

%files -n texlive-oscola
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/oscola/
%{_texdir}/texmf-dist/tex/latex/oscola/

%files -n texlive-oscola-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/oscola/

%files -n texlive-old-arrows
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/old-arrows/
%{_texdir}/texmf-dist/fonts/enc/dvips/old-arrows/
%{_texdir}/texmf-dist/fonts/map/dvips/old-arrows/
%{_texdir}/texmf-dist/fonts/tfm/public/old-arrows/
%{_texdir}/texmf-dist/fonts/type1/public/old-arrows/
%{_texdir}/texmf-dist/tex/latex/old-arrows/

%files -n texlive-old-arrows-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/old-arrows/

%files -n texlive-obnov
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/obnov/
%{_texdir}/texmf-dist/fonts/tfm/public/obnov/
%{_texdir}/texmf-dist/tex/latex/obnov/

%files -n texlive-obnov-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/obnov/

%files -n texlive-ocherokee
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/ocherokee/
%{_texdir}/texmf-dist/fonts/map/dvips/ocherokee/
%{_texdir}/texmf-dist/fonts/ofm/public/ocherokee/
%{_texdir}/texmf-dist/fonts/ovf/public/ocherokee/
%{_texdir}/texmf-dist/fonts/ovp/public/ocherokee/
%{_texdir}/texmf-dist/fonts/tfm/public/ocherokee/
%{_texdir}/texmf-dist/fonts/type1/public/ocherokee/
%{_texdir}/texmf-dist/omega/ocp/ocherokee/
%{_texdir}/texmf-dist/tex/lambda/ocherokee/

%files -n texlive-ocherokee-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/omega/ocherokee/

%files -n texlive-ocr-b
%{_texdir}/texmf-dist/fonts/source/public/ocr-b/
%{_texdir}/texmf-dist/fonts/tfm/public/ocr-b/

%files -n texlive-ocr-b-doc
%{_texdir}/texmf-dist/doc/fonts/ocr-b/

%files -n texlive-ocr-b-outline
%{_datadir}/fonts/ocr-b-outline
%{_texdir}/texmf-dist/fonts/map/dvips/ocr-b-outline/
%{_texdir}/texmf-dist/fonts/opentype/public/ocr-b-outline/
%{_texdir}/texmf-dist/fonts/type1/public/ocr-b-outline/

%files -n texlive-ocr-b-outline-doc
%{_texdir}/texmf-dist/doc/fonts/ocr-b-outline/

%files -n texlive-ogham
%{_texdir}/texmf-dist/fonts/source/public/ogham/
%{_texdir}/texmf-dist/fonts/tfm/public/ogham/

%files -n texlive-ogham-doc
%{_texdir}/texmf-dist/doc/fonts/ogham/

%files -n texlive-oinuit
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/oinuit/
%{_texdir}/texmf-dist/fonts/ofm/public/oinuit/
%{_texdir}/texmf-dist/fonts/ovf/public/oinuit/
%{_texdir}/texmf-dist/fonts/tfm/public/oinuit/
%{_texdir}/texmf-dist/fonts/type1/public/oinuit/
%{_texdir}/texmf-dist/omega/ocp/oinuit/
%{_texdir}/texmf-dist/omega/otp/oinuit/
%{_texdir}/texmf-dist/tex/lambda/oinuit/

%files -n texlive-oinuit-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/oinuit/

%files -n texlive-oldlatin
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/

%files -n texlive-oldlatin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/oldlatin/

%files -n texlive-oldstandard
%{_texdir}/texmf-dist/fonts/opentype/public/oldstandard/
%{_texdir}/texmf-dist/fonts/enc/dvips/oldstandard/
%{_texdir}/texmf-dist/fonts/map/dvips/oldstandard/
%{_texdir}/texmf-dist/fonts/tfm/public/oldstandard/
%{_texdir}/texmf-dist/fonts/vf/public/oldstandard/
%{_texdir}/texmf-dist/tex/latex/oldstandard/

%files -n texlive-oldstandard-doc
%{_texdir}/texmf-dist/doc/fonts/oldstandard/

%files -n texlive-opensans
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/opensans/
%{_texdir}/texmf-dist/fonts/enc/dvips/opensans/
%{_texdir}/texmf-dist/fonts/map/dvips/opensans/
%{_texdir}/texmf-dist/fonts/tfm/public/opensans/
%{_texdir}/texmf-dist/fonts/truetype/public/opensans/
%{_texdir}/texmf-dist/fonts/type1/public/opensans/
%{_texdir}/texmf-dist/fonts/vf/public/opensans/
%{_texdir}/texmf-dist/tex/latex/opensans/

%files -n texlive-opensans-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/opensans/

%files -n texlive-orkhun
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/orkhun/
%{_texdir}/texmf-dist/fonts/tfm/public/orkhun/

%files -n texlive-orkhun-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/orkhun/

%files -n texlive-overlock
%license ofl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/overlock/
%{_texdir}/texmf-dist/fonts/map/dvips/overlock/
%{_texdir}/texmf-dist/fonts/tfm/muhafara/overlock/
%{_texdir}/texmf-dist/fonts/truetype/muhafara/overlock/
%{_texdir}/texmf-dist/fonts/type1/muhafara/overlock/
%{_texdir}/texmf-dist/fonts/vf/muhafara/overlock/
%{_texdir}/texmf-dist/tex/latex/overlock/

%files -n texlive-overlock-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/overlock/

%files -n texlive-othello
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/othello/
%{_texdir}/texmf-dist/fonts/tfm/public/othello/
%{_texdir}/texmf-dist/tex/latex/othello/

%files -n texlive-othello-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/othello/

%files -n texlive-othelloboard
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/othelloboard/

%files -n texlive-othelloboard-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/othelloboard/

%files -n texlive-ofs
%license knuth.txt
%{_texdir}/texmf-dist/tex/generic/ofs/

%files -n texlive-ofs-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/generic/ofs/

%files -n texlive-ntheorem-vn-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ntheorem-vn/

%files -n texlive-ntgclass
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ntgclass/

%files -n texlive-ntgclass-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ntgclass/

%files -n texlive-noconflict
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/noconflict/

%files -n texlive-noconflict-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/noconflict/

%files -n texlive-noindentafter
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/noindentafter/

%files -n texlive-noindentafter-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/noindentafter/

%files -n texlive-noitcrul
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/noitcrul/

%files -n texlive-noitcrul-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/noitcrul/

%files -n texlive-nolbreaks
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/nolbreaks/

%files -n texlive-nolbreaks-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/nolbreaks/

%files -n texlive-nomencl
%license lppl1.txt
%{_texdir}/texmf-dist/makeindex/nomencl/
%{_texdir}/texmf-dist/tex/latex/nomencl/

%files -n texlive-nomencl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nomencl/

%files -n texlive-nomentbl
%license lppl1.txt
%{_texdir}/texmf-dist/makeindex/nomentbl/
%{_texdir}/texmf-dist/tex/latex/nomentbl/

%files -n texlive-nomentbl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nomentbl/

%files -n texlive-nonfloat
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/nonfloat/

%files -n texlive-nonfloat-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/nonfloat/

%files -n texlive-nonumonpart
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/nonumonpart/

%files -n texlive-nonumonpart-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/nonumonpart/

%files -n texlive-nopageno
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nopageno/

%files -n texlive-nopageno-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nopageno/

%files -n texlive-notes
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/notes/

%files -n texlive-notes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/notes/

%files -n texlive-notoccite
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/notoccite/

%files -n texlive-notoccite-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/notoccite/

%files -n texlive-nowidow
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nowidow/

%files -n texlive-nowidow-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nowidow/

%files -n texlive-nox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nox/

%files -n texlive-nox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nox/

%files -n texlive-ntheorem
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ntheorem/

%files -n texlive-ntheorem-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ntheorem/

%files -n texlive-nuc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nuc/

%files -n texlive-nuc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nuc/

%files -n texlive-numericplots
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/numericplots/

%files -n texlive-numericplots-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/numericplots/

%files -n texlive-numberedblock
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/numberedblock/

%files -n texlive-numberedblock-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/numberedblock/

%files -n texlive-numname
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/numname/

%files -n texlive-numname-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/numname/

%files -n texlive-numprint
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/numprint/

%files -n texlive-numprint-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/numprint/

%files -n texlive-ocg-p
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ocg-p/

%files -n texlive-ocg-p-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ocg-p/

%files -n texlive-ocgx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ocgx/

%files -n texlive-ocgx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ocgx/

%files -n texlive-ocgx2
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ocgx2/

%files -n texlive-ocgx2-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ocgx2/

%files -n texlive-ocr-latex
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/ocr-latex/

%files -n texlive-ocr-latex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ocr-latex/

%files -n texlive-octavo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/octavo/

%files -n texlive-octavo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/octavo/

%files -n texlive-oldstyle
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/oldstyle/

%files -n texlive-oldstyle-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/oldstyle/

%files -n texlive-onlyamsmath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/onlyamsmath/

%files -n texlive-onlyamsmath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/onlyamsmath/

%files -n texlive-opcit
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/opcit/
%{_texdir}/texmf-dist/tex/latex/opcit/

%files -n texlive-opcit-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/opcit/

%files -n texlive-optional
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/optional/

%files -n texlive-optional-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/optional/

%files -n texlive-outline
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/outline/

%files -n texlive-outline-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/outline/

%files -n texlive-outliner
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/outliner/

%files -n texlive-outliner-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/outliner/

%files -n texlive-outlines
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/outlines/

%files -n texlive-outlines-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/outlines/

%files -n texlive-overpic
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/overpic/

%files -n texlive-overpic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/overpic/

%files -n texlive-odsfile
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/lualatex/odsfile/

%files -n texlive-odsfile-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/odsfile/

%files -n texlive-ot-tableau
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ot-tableau/

%files -n texlive-ot-tableau-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ot-tableau/

%files -n texlive-oubraces
%{_texdir}/texmf-dist/tex/latex/oubraces/

%files -n texlive-oubraces-doc
%{_texdir}/texmf-dist/doc/latex/oubraces/

%files -n texlive-otibet
%{_texdir}/texmf-dist/fonts/ofm/public/otibet/
%{_texdir}/texmf-dist/fonts/ovf/public/otibet/
%{_texdir}/texmf-dist/fonts/ovp/public/otibet/
%{_texdir}/texmf-dist/fonts/source/public/otibet/
%{_texdir}/texmf-dist/fonts/tfm/public/otibet/
%{_texdir}/texmf-dist/omega/ocp/otibet/
%{_texdir}/texmf-dist/omega/otp/otibet/
%{_texdir}/texmf-dist/tex/latex/otibet/

%files -n texlive-otibet-doc
%{_texdir}/texmf-dist/doc/latex/otibet/

%files -n texlive-nostarch
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/nostarch/
%{_texdir}/texmf-dist/makeindex/nostarch/
%{_texdir}/texmf-dist/tex/latex/nostarch/

%files -n texlive-nostarch-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nostarch/

%files -n texlive-nrc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nrc/

%files -n texlive-nrc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nrc/

%files -n texlive-onrannual
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/onrannual/

%files -n texlive-onrannual-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/onrannual/

%files -n texlive-opteng
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/opteng/

%files -n texlive-opteng-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/opteng/

%files -n texlive-objectz
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/objectz/

%files -n texlive-objectz-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/objectz/

%files -n texlive-normalcolor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/normalcolor/

%files -n texlive-normalcolor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/normalcolor/

%files -n texlive-noto-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/noto/

%files -n texlive-noto
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/noto/
%{_texdir}/texmf-dist/fonts/opentype/google/noto/
%{_texdir}/texmf-dist/fonts/truetype/google/noto/
%{_texdir}/texmf-dist/fonts/map/dvips/noto/
%{_texdir}/texmf-dist/fonts/tfm/google/noto/
%{_texdir}/texmf-dist/fonts/vf/google/noto/
%{_texdir}/texmf-dist/fonts/enc/dvips/noto/
%{_texdir}/texmf-dist/fonts/type1/google/noto/

%files -n texlive-nucleardata-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nucleardata/

%files -n texlive-nucleardata
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nucleardata/

%files -n texlive-nwejm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nwejm/

%files -n texlive-nwejm
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nwejm/

%files -n texlive-optidef-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/optidef/

%files -n texlive-optidef
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/optidef/

%files -n texlive-options-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/options/

%files -n texlive-options
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/options/

%files -n texlive-obsolete

%files -n texlive-nodetree
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/luatex/nodetree/
%{_texdir}/texmf-dist/tex/luatex/nodetree/

%files -n texlive-notespages
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/notespages/
%{_texdir}/texmf-dist/tex/latex/notespages/

%files -n texlive-notestex
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/notestex/
%{_texdir}/texmf-dist/tex/latex/notestex/

%files -n texlive-novel
%license lppl1.3.txt ofl.txt
%doc %{_texdir}/texmf-dist/doc/lualatex/novel/
%{_texdir}/texmf-dist/fonts/opentype/novel/
%{_texdir}/texmf-dist/tex/lualatex/novel/

%files -n texlive-numnameru
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/numnameru/
%{_texdir}/texmf-dist/tex/latex/numnameru/

%files -n texlive-numspell
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/numspell/
%{_texdir}/texmf-dist/tex/latex/numspell/

%files -n texlive-octave
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/octave/
%{_texdir}/texmf-dist/tex/latex/octave/

%files -n texlive-olsak-misc
%doc %{_texdir}/texmf-dist/doc/generic/olsak-misc/
%{_texdir}/texmf-dist/tex/generic/olsak-misc/

%files -n texlive-notex-bst
%{_texdir}/texmf-dist/bibtex/bst/notex-bst/

%files -n texlive-onedown
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/onedown/
%doc %{_texdir}/texmf-dist/doc/latex/onedown/

%files -n texlive-oplotsymbl
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/oplotsymbl/
%doc %{_texdir}/texmf-dist/doc/latex/oplotsymbl/

%files -n texlive-outlining
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/outlining/
%doc %{_texdir}/texmf-dist/doc/latex/outlining/

%files -n texlive-overlays
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/overlays/
%doc %{_texdir}/texmf-dist/doc/latex/overlays/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
