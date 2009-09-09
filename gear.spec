# Copyright (C) 2006-2008  Dmitry V. Levin <ldv@altlinux.org>

Name: gear
Version: 1.5.3
Release: alt1

Summary: Get Every Archive from git package Repository
License: GPLv2+
Group: Development/Other
Url: http://www.altlinux.org/Gear
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

# due to gear-srpmimport.
Requires: faketime

# due to git-diff-tree --no-ext-diff
Requires: git-core >= 0:1.5.3

# due to quote_shell_args()
Requires: libshell >= 0:0.1.0

# hasher>=1.0.30 supports tar packages made by gear utility.
Conflicts: hasher < 0:1.0.30

BuildPreReq: asciidoc, git-core, help2man, libshell >= 0:0.0.3-alt1
%{?!_without_check:%{?!_disable_check:BuildRequires: lzma-utils, unzip}}

%description
This package contains utilities for building RPM packages from GEAR
repositories and managing GEAR repositories.
See %_docdir/%name-%version/QUICKSTART.ru_RU.UTF-8 for details.

%prep
%setup -q

%build
%make_build
asciidoc ABOUT.ru.utf8
asciidoc QUICKSTART.ru.utf8

%check
make check

%install
%make_install install DESTDIR=%buildroot
install -pDm644 contrib/gear-bash_completion %buildroot/etc/bash_completion.d/gear

%files
%config /etc/bash_completion.d/*
%_bindir/*
%_mandir/man?/*
%doc QUICKSTART* ABOUT*

%changelog
* Fri Mar 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.3-alt1
- gear-create-tag: Fixed usage, added --time option (Alexey Gladkov).
- gear-srpmimport: Made --quiet mode more quiet.
- gear-srpmimport: Enhanced changelog name parser.
- gear-commit: Added --no-edit option (Alexey Gladkov).
- gear-remote: Fixed options order (Alexey Gladkov; closes: #19073).
- Added URL, updated %%description (closes: #18852).

* Wed Jan 28 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.2-alt1
- gear: make_compress(): Added keywords support in the name option (Alexey Gladkov).
- gear-update-tag: Added 'compress' directive (Alexey Gladkov; closes: #17624).
- gear-remote: Added --remote-repo (Alexey Gladkov; closes: #17865).
- gear: Fixed "diff" rule misbehavior (closes: ALT#17751).
- gear (get_tar_name, get_diff_name): Do check_path on modified path.
- gear-update-tag: chdir to toplevel directory (closes: ALT#18029).
- gear-commit: Unquote %%%% in changelog text.
- gear-srpmimport, gear-update: Use .gitattributes export-ignore
  instead of .gitignore to import empty directories.
- ABOUT.ru, QUICKSTART.ru: Converted from koi8r to utf8.

* Thu Oct 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.1-alt1
- gear-commit: Fix help message (Alexey Gladkov; closes: #16690).
- gear-changelog: Use git-config if GIT_AUTHOR_* is not set (Alexey Gladkov; closes: #16705).
- gear-update (Alexey Gladkov; closes: #17075):
  + Don't try to remove destdir in empty repository.
  + Remove temp directory before adding destdir into repository.
- gear-sh-functions.in (Alexey Froloff):
  + gear_config_option: New function, to use git config for option storage.
  + Fetch --verbose and --quiet options defaults from git config.
- gear-create-tag: Fetch --name and --message defaults from git config (Alexey Froloff).
- gear-changelog: Fetch releaser name and email defaults from git config (Alexey Froloff).
- gear: Fetch compress method and --rules options from git config (Alexey Froloff).
- Fixed signal handler exit code.
- gear-sh-functions.in (get_NVR_from_spec), gear-srpmimport:
  Allow and strip trailing whitespaces in name/version/release.
- gear: Implement keywords substitution in directory names.

* Fri Aug 01 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- gear-changelog: New utility for preparing changelog records
  based on git commit messages (Alexey Gladkov).
- gear-update-tag: New --verify option (Alexey Froloff).
- gear-update: Add .gitignore file into empty directories like
  gear-srpmimport does (Alexey Gladkov).
- gear: New "compress" rule (Alexey Gladkov, me).
- Added bash-completion functions for gear utilities (Alexey Gladkov).
- gear-merge: Numerous changes (Alexey Froloff, Alexey Gladkov).
- Various manpage cleanups (me).

* Mon Mar 17 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- Changes made by Alexey Gladkov:
  + gear-merge: New utility to merge branches.
  + gear-merge-rules(5): New man page which describes
    the .gear/merge file format.
  + gear --command: New option.
  + gear-command-hasher, gear-command-rpmbuild, gear-command-tar:
    New helpers.
  + gear-hsh, gear-rpm, gear-buildreq: New utilities which
    hopefully provide more convenient user interface than
    old --hasher and --rpmbuild options.
  + gear-command-remote-build: New helper.
  + gear-remote, gear-remote-hsh, gear-remote-rpm: New utilities.
  + gear-commit: Use getopt from libshell.
- My changes:
  + gear-create-tag: Fixed -u option support.
  + gear-srpmimport: Add empty .gitignore file to each empty directory.
  + Made readlink(1) usage secure.
  + gear-srpmimport: Added support for git-commit versions
    which do not handle --fast option.
  + Use shell-error, shell-quote and shell-args from libshell
    to replace several functions originally developed within
    hasher and gear projects.
  + Do not use dashed form of git commands.
  + gear: Implemented empty archive suffix support.
  + Renamed: *.ru_RU.KOI8-R -> *.ru.koi8
  + QUICKSTART.ru.koi8: Formatted for AsciiDoc.
  + ABOUT.ru.koi8: Imported thesis about gear from Protva2007
    in AsciiDoc format.
  + Packaged asciidoc-generated QUICKSTART.ru.html and ABOUT.ru.html files.
  + gear-update-tag: Added -q/--quiet and --no-clean options.
  + gear-update-tag: Changed --all option to imply --clean.
- Other minor fixes and cleanups, see git log for details.

* Fri Nov 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- gear-create-tag:
  + Enabled keyword substitution in --name and ----message options (ldv).
- gear-sh-functions.in (get_NVR_from_spec):
  + Added minimal support for RPM macros (vsu).

* Tue Oct 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Added .gear directory support (ldv).
- Extended rules syntax: made whitespaces between directive
  and its parameters optional (legion, ldv).
- gear-create-tag (show_help): Fixed options output (ldv).
- gear (make_diff): Pass additional options to git-diff-tree,
  this change makes "diff" directive complete (ldv).
- Install gear-sh-functions without execute permissions set (ldv).
- gear-commit: Fixed unbound variable error (legion, #13057).
- gear-update: Added --create option (legion).
- gear-update: Added check for initial commit and
  for changed files in the index (legion, ldv).
- gear-hsh-build (raorn):
  + Honor "prefix" option from ~/.hasher/config.
  + Enhanced --repo handling.
  + exit_handler: Show path to hasher repo if build has failed.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.7-alt1
- gear-srpmimport: Pass --fast option to git-commit (ldv).
- gear-update: Added --all and --exclude options (legion).

* Wed Aug 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.6-alt1
- gear-update (legion):
  + Added cpio* types support.
  + Allowed update of top directory.
- gear:
  + Robustify --commit (ldv).
- gear, gear-srpmimport, gear-update:
  + Run grep in C locale, run sort in C collation (ldv).
- gear-create-tag:
  + New utility, creates a signed release tag object (legion, ldv).

* Sun May 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- gear-srpmimport:
  + Do not perform a noop merge (#11721).
  + Fixed import of archives with non-directory toplevel files.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- gear-sh-functions.in (chdir_to_toplevel): New function.
- gear, gear-srpmimport, gear-update: Use chdir_to_toplevel().
- gear-commit: Chdir to toplevel directory early.

* Mon Mar 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Added gear-rules(5) man page which describes the .gear-rules
  file format (vsu).

* Sun Mar 11 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Changed "git-COMMAND" style commands to "git COMMAND" style.
- gear-update: Suppressed "git rm" output.
- gear-update, gear-update-tag: Separated "git COMMAND"
  command-line options from lists of files where appropriate.
- QUICKSTART.ru_RU.KOI8-R:
  + Reworded git config recommendations using "git config" commands.
  + Updated examples.

* Sun Mar 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- gear: Fixed suffix support (ldv, #11008).

* Wed Feb 28 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- gear-update: New utility, replaces gear-update-archive and
  gear-update-directory (legion, ldv).
- gear-upload: Move to separate package, girar-utils (ldv).
- gear: Chdir to toplevel directory early (ldv).
- gear-srpmimport (ldv):
  + Chdir to toplevel directory early.
  + If --quiet option given, do commit and merge quietly.
  + Rename --no-untar option to --no-unpack.
  + Rewrite archive importer:
    - Use file(1) to recognize file types
      instead of suffix-based switch.
    - Handle zip archives.
    - Support arbitrary archive names.
- QUICKSTART.ru_RU.KOI8-R: Mention ~/.gitconfig (azol).

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- gear-update-tag: Fix temporary directory removal (ldv).
- gear-update-tag: Treat "zip" directive as "tar" (raorn).
- gear: Implement suffix= option for tar-like rules (george).

* Wed Nov 22 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- gear, gear-commit, gear-sh-functions.in:
  Reworked to implement .gear-rules "tags:" directive and
  .gear-tags directory support (vsu, raorn).
- gear-update-tag:
  New utility, updates list of stored tags
  in the package repository (vsu).
- gear-update-archive:
  Avoid loss of source files due to .gitignore (vsu).
- gear-release:
  Removed unneeded utility, the idea of release tags
  seems to be dead-end (ldv).
- Renamed info() to msg_info() to avoid ambiguity and
  unwanted package requirements (ldv).
- QUICKSTART.ru_RU.KOI8-R: Fix typos (#10229).
- gear-srpmimport:
  Removed implicit requirement for --branch (ldv, #10274).
- gear:
  Added keyword substitution in directory name (ldv, #10091).
  Replaced deprecated "git-tar-tree" with "git-archive --format=tar" (ldv).
  Implemented zip archive type support (raorn).
- gear-upload:
  New utility to ease initial upload of git repositories to git.alt (legion).

* Thu Oct 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- Update copyright information.
- Add fresh git-core to package requirements.
- gear:
  + Process exclude directives without warnings (vsu).
- gear-sh-functions.in:
  + Fix checks for multiple specfiles (vsu).
- gear-release:
  + Create tags in refs/releases/ directory (ldv).
- gear-update-archive:
  + Fix old source removal (ldv).
  + Fix check for untracked or modified files (legion).
  + Implement top directory update (legion).
  + Fix destination directory validation (legion).
  + Fix typos (vsu).
- gear-hsh-build:
  + more flexible hasher support (raorn).
  + also pass --repo option to hasher (raorn).
  + honor "target" option from hasher config (raorn).
  + use $GIT_DIR/$CWD if no repositories given (raorn).
- Makefile:
  + Specify the program source for man pages (vsu).
  + Remove boldface from the NAME section of man pages (vsu).
- gear.1.inc:
  + Document operating modes of gear (vsu).
  + Document current limitations of gear (vsu).
- gear-commit.1.inc:
  + Fix short description (ldv).
- gear-update-archive.1.inc, gear-update-directory.1.inc:
  + Fix typos (vsu).

* Fri Sep 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- gear:
  + New option: --update-spec (legion).
- gear-commit:
  + New option: --spec (legion).
- gear-release:
  + New option: --create (legion).
- gear-update:
  + Rename to gear-update-archive (legion).
- gear-hsh-build:
  + New utility (raorn).

* Mon Aug 28 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- gear-release: Fix typo in option handling (legion).
- gear-update: New utility (legion, ldv).

* Tue Aug 22 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- Initial revision.
