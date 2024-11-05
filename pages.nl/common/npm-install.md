# npm install

> Install node packages.
> Meer informatie: <https://docs.npmjs.com/cli/commands/npm-install>.

- Install dependencies listed in package.json:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install {{pakket_naam}}@{{version}}`

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm install {{pakket_naam}} {{-D|--save-dev}}`

- Download the latest version of a package and install it globally:

`npm install {{-g|--global}} {{pakket_naam}}`
