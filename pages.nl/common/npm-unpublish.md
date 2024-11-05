# npm unpublish

> Remove a package from the npm registry.
> Meer informatie: <https://docs.npmjs.com/cli/v8/commands/npm-unpublish>.

- Unpublish a specific package version:

`npm unpublish {{pakket_naam}}@{{version}}`

- Unpublish the entire package:

`npm unpublish {{pakket_naam}} --force`

- Unpublish a package that is scoped:

`npm unpublish @{{scope}}/{{pakket_naam}}`

- Specify a timeout period before unpublishing:

`npm unpublish {{pakket_naam}} --timeout {{time_in_milliseconds}}`

- To prevent accidental unpublishing, use the `--dry-run` flag to see what would be unpublished:

`npm unpublish {{pakket_naam}} --dry-run`
