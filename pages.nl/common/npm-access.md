# npm access

> Set access level on published packages.
> Meer informatie: <https://docs.npmjs.com/cli/npm-access>.

- List packages for a user or scope:

`npm access list packages {{user|scope|scope:team}} {{pakket_naam}}`

- List collaborators on a package:

`npm access list collaborators {{pakket_naam}} {{gebruikersnaam}}`

- Get status of a package:

`npm access get status {{pakket_naam}}`

- Set package status (public or private):

`npm access set status={{public|private}} {{pakket_naam}}`

- Grant access to a package:

`npm access grant {{read-only|read-write}} {{scope:team}} {{pakket_naam}}`

- Revoke access to a package:

`npm access revoke {{scope:team}} {{pakket_naam}}`

- Configure two-factor authentication requirement:

`npm access set mfa={{none|publish|automation}} {{pakket_naam}}`
