# npm unstar

> Remove the favorite/star mark from a package.
> Meer informatie: <https://docs.npmjs.com/cli/commands/npm-unstar>.

- Unstar a public package from the default registry:

`npm unstar {{pakket_naam}}`

- Unstar a package within a specific scope:

`npm unstar @{{scope}}/{{pakket_naam}}`

- Unstar a package from a specific registry:

`npm unstar {{pakket_naam}} --registry={{registry_url}}`

- Unstar a private package that requires authentication:

`npm unstar {{pakket_naam}} --auth-type={{legacy|oauth|web|saml}}`

- Unstar a package by providing an OTP for two-factor authentication:

`npm unstar {{pakket_naam}} --otp={{otp}}`

- Unstar a package with a specific logging level:

`npm unstar {{pakket_naam}} --loglevel={{silent|error|warn|notice|http|timing|info|verbose|silly}}`
