# npm-org

> Manage organizations.
> Meer informatie: <https://docs.npmjs.com/cli/commands/npm-org>.

- Add a new user to an organization:

`npm org set {{organisatie_naam}} {{gebruikersnaam}}`

- Change a user's role in an organization:

`npm org set {{organisatie_naam}} {{gebruikersnaam}} {{developer|admin|owner}}`

- Remove a user from an organization:

`npm org rm {{organisatie_naam}} {{gebruikersnaam}}`

- List all users in an organization:

`npm org ls {{organisatie_naam}}`

- List all users in an organization, output in JSON format:

`npm org ls {{organisatie_naam}} --json`

- Display a user's role in an organization:

`npm org ls {{organisatie_naam}} {{gebruikersnaam}}`
