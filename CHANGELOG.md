None (1.7.1) unstable; urgency=medium

  * Features
    * 
      * 6a75dfb This is version-plus now.
    * packaging.version
      * 75a82f2 Migrate to latest version
    * StrictVersion
      * 8702bb5 Wrap packaging Version in StrictVersion, implement modification
    * Deps
      * fe8c1ce Migrate to packaging from distutils
    * CI
      * a1d30ee Use python-virtualenv instead of build in
      * 5db44bf Install python3-venv for debian
      * 76f0ef4 Test in env
      * eeed86d Debian needs dh-python
    * Mark
      * b3b958f Allow --force to force version when uncommited files are found
    * Changelog
      * afb2ab8 Added option to generate whole changelog
      * c73553c Added simple changelog CLI
      * c31b6f2 Implement WhatIsNew changelog generator
      * 634228d Added Debian changelog generator for #2
    * Log
      * 88d86db Simplify log format for better UX
    * Check
      * dfa87a7 Added option to force older version number
  * Fixes
    * mark_version_files
      * 19e379f Fix bug with incorrectly replaced version string
    * 
      * 6bf6ac3 Return StrictVersion directly
      * 0095e8f Pass StrictVersion object, not str
      * 5032da7 Files version check
      * 1c71713 Fix when advancing major version, patch version was not reset
    * StrictVersion
      * 4dcb85d Override _key too
    * CI
      * 031d254 Do not install python-all in Debian
      * fab2e58 Fix arch test
      * 926c266 Remove old versions from arch repo correctly
      * 846970f Fix debian repo path
      * 7a6e8c9 Remove packagetest
    * Sematic
      * 348ad82 Fix crash when no tags exists
      * faba815 Handle situations when tag is not created yet
    * Parsing
      * 6723ad3 Fixes crash when patch version is not provided
    * Changelog
      * 2286ead Fix when tagger info is missing
      * ff96e69 Use tag info only when avaiable
      * a501512 Fixes in chagelog genreator to include tags with no matched commits
      * 073b239 Debian changelog, generate date correctly
      * e53e115 Pull commits correctly when HEAD is used
      * a88c2f6 Do not crash when original changelog was not found
      * 7ab98b6 Fix mkdir in Debian changelog generator
    * WhatIsNew
      * e36dae8 Call makdir only when path is in dir
      * b4ab9d2 Fix crash when there is no tag in git repo

 -- Adam Schubert <adam.schubert@sg1-game.net>  Thu, 13 Aug 2026 22:48:35 +0000

version-plus (1.7.0) unstable; urgency=medium

  * Rebrand the distributable package as Version+ (`version-plus`).
  * Add `version init` discovery for common project metadata.
  * Add safe, non-interactive dry-run behavior and CLI regression tests.
  * Add Python 3.9-3.14 CI and trusted PyPI publishing.
  * Modernize packaging, documentation, and Arch Linux builds.

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 14 Aug 2026 00:00:00 +0200

None (1.6.1) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 17 Feb 2026 19:55:36 +0000

None (1.6.0) unstable; urgency=medium

  * Features
    * packaging.version
      * 75a82f2 Migrate to latest version

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 17 Feb 2026 19:30:22 +0000

None (1.5.7) unstable; urgency=medium

  * Fixes
    * mark_version_files
      * 19e379f Fix bug with incorrectly replaced version string

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 22 Mar 2025 22:19:01 +0000

None (1.5.6) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 10 Jan 2025 18:51:33 +0000

None (1.5.5) unstable; urgency=medium

  * Fixes
    * 
      * 6bf6ac3 Return StrictVersion directly

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 01 Oct 2024 18:39:22 +0000

None (1.5.4) unstable; urgency=medium

  * Fixes
    * 
      * 0095e8f Pass StrictVersion object, not str

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 01 Oct 2024 18:28:07 +0000

None (1.5.3) unstable; urgency=medium

  * Fixes
    * 
      * 5032da7 Files version check

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 01 Oct 2024 18:16:22 +0000

None (1.5.2) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sun, 22 Sep 2024 21:38:32 +0000

None (1.5.1) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sun, 22 Sep 2024 21:31:58 +0000

None (1.5.0) unstable; urgency=medium

  * Fixes
    * StrictVersion
      * 4dcb85d Override _key too
  * Features
    * StrictVersion
      * 8702bb5 Wrap packaging Version in StrictVersion, implement modification
    * Deps
      * fe8c1ce Migrate to packaging from distutils

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sun, 22 Sep 2024 21:26:18 +0000

None (1.4.3) unstable; urgency=medium

  * Features
    * CI
      * a1d30ee Use python-virtualenv instead of build in

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 29 Apr 2024 10:51:04 +0000

None (1.4.2) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 29 Apr 2024 08:48:19 +0000

None (1.4.1) unstable; urgency=medium

  * Fixes
    * CI
      * 031d254 Do not install python-all in Debian
  * Features
    * CI
      * 5db44bf Install python3-venv for debian
      * 76f0ef4 Test in env

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 10 Oct 2023 20:08:56 +0000


None (1.4) unstable; urgency=medium

  * Features
    * Mark
      * b3b958f Allow --force to force version when uncommited files are found

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 10 Oct 2023 12:04:10 +0200

None (1.4) unstable; urgency=medium

  * Features
    * Mark
      * b3b958f Allow --force to force version when uncommited files are found

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 10 Oct 2023 10:04:10 +0000

None (1.3.9) unstable; urgency=medium

  * Fixes
    * CI
      * fab2e58 Fix arch test

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 10 May 2023 18:23:10 +0000

None (1.3.8) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 10 May 2023 18:14:03 +0000

None (1.3.7) unstable; urgency=medium

  * Fixes
    * Sematic
      * 348ad82 Fix crash when no tags exists

 -- Adam Schubert <adam.schubert@sg1-game.net>  Thu, 14 Jul 2022 20:51:12 +0000

None (1.3.6) unstable; urgency=medium

  * Fixes
    * Parsing
      * 6723ad3 Fixes crash when patch version is not provided

 -- Adam Schubert <adam.schubert@sg1-game.net>  Thu, 14 Jul 2022 15:10:45 +0000

None (1.3.5) unstable; urgency=medium

  * Fixes
    * Changelog
      * 2286ead Fix when tagger info is missing

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 02 Apr 2022 18:12:40 +0000

None (1.3.4) unstable; urgency=medium

  * Fixes
    * Changelog
      * ff96e69 Use tag info only when avaiable
      * a501512 Fixes in chagelog genreator to include tags with no matched commits

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 02 Apr 2022 19:57:32 +0200


None (1.3.3) unstable; urgency=medium

  * Fixes
    * Changelog
      * 073b239 Debian changelog, generate date correctly

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 02 Apr 2022 19:06:10 +0200


None (1.3.2) unstable; urgency=medium

  * Fixes
    * Changelog
      * e53e115 Pull commits correctly when HEAD is used

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 16:59:16 +0200


None (1.3.1) unstable; urgency=medium

  * Fixes
    * Sematic
      * faba815 Handle situations when tag is not created yet

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 16:46:57 +0200


None (1.3) unstable; urgency=medium

  * Features
    * Changelog
      * afb2ab8 Added option to generate whole changelog

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 16:18:22 +0200


None (1.2.18) unstable; urgency=medium

  * Fixes
    * Changelog
      * a88c2f6 Do not crash when original changelog was not found

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 14:03:30 +0200


None (1.2.17) unstable; urgency=medium

  * Fixes
    * Changelog
      * 7ab98b6 Fix mkdir in Debian changelog generator

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 13:56:25 +0200


None (1.2.16) unstable; urgency=medium

  * Features
    * Changelog
      * c73553c Added simple changelog CLI

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 13:50:54 +0200


None (1.2.15) unstable; urgency=medium

  * Fixes
    * WhatIsNew
      * e36dae8 Call makdir only when path is in dir

 -- Adam Schubert <adam.schubert@sg1-game.net>  Fri, 01 Apr 2022 12:55:15 +0200


None (1.2.14) unstable; urgency=medium

  * Fixes
    * 
      * 1c71713 Fix when advancing major version, patch version was not reset

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 13 Oct 2021 23:46:41 +0200


None (1.2.13) unstable; urgency=medium

  * Fixes
    * CI
      * 926c266 Remove old versions from arch repo correctly

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 23 Aug 2021 18:41:48 +0200


None (1.2.12) unstable; urgency=medium

  * Features
    * Log
      * 88d86db Simplify log format for better UX

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 23 Aug 2021 18:31:38 +0200


None (1.2.11) unstable; urgency=medium

  * Features
    * CI
      * eeed86d Debian needs dh-python
  * Fixes
    * CI
      * 846970f Fix debian repo path

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 23 Aug 2021 17:21:20 +0200


None (1.2.10) unstable; urgency=medium

  * Features
    * Check
      * dfa87a7 Added option to force older version number

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 23 Aug 2021 16:29:44 +0200


None (1.2.9) unstable; urgency=medium

  * Fixes
    * CI
      * 7a6e8c9 Remove packagetest

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 15 Jun 2021 23:51:10 +0200


None (1.2.8) unstable; urgency=medium

  * Fixes
    * WhatIsNew
      * b4ab9d2 Fix crash when there is no tag in git repo

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 15 Jun 2021 23:10:53 +0200


None (1.2.7) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 02 Apr 2022 18:11:06 +0000


None (1.2.6) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 02 Apr 2022 18:11:06 +0000


None (1.2.5) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sat, 02 Apr 2022 18:11:06 +0000


None (1.2.4) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 17 Feb 2020 19:14:55 +0100


None (1.2.3) unstable; urgency=medium

  * Features
    * Changelog
      * c31b6f2 Implement WhatIsNew changelog generator

 -- Adam Schubert <adam.schubert@sg1-game.net>  Mon, 17 Feb 2020 19:14:28 +0100


None (1.2.2) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 19 Nov 2019 04:50:51 +0100


None (1.2.1) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 19 Nov 2019 04:50:34 +0100


None (1.2) unstable; urgency=medium

  * Features
    * Changelog
      * 634228d Added Debian changelog generator for #2

 -- Adam Schubert <adam.schubert@sg1-game.net>  Thu, 24 Oct 2019 01:07:02 +0200


None (1.1.25) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 02 Oct 2019 06:38:29 +0200


None (1.1.24) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Sun, 18 Aug 2019 13:46:38 +0200


None (1.1.23) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Thu, 23 Aug 2018 03:17:13 +0200


None (1.1.22) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 04:03:34 +0200


None (1.1.21) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:58:43 +0200


None (1.1.20) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:57:57 +0200


None (1.1.19) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:57:18 +0200


None (1.1.14) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:47:14 +0200


None (1.1.13) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:46:19 +0200


None (1.1.12) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:44:52 +0200


None (1.1.11) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Wed, 06 Jun 2018 01:41:38 +0200


None (1.1.10) unstable; urgency=medium

  * Nothing worth mentioning

 -- Adam Schubert <adam.schubert@sg1-game.net>  Tue, 05 Jun 2018 22:50:24 +0200
