# npm star

> Mark a package as favorite.
> Meer informatie: <https://docs.npmjs.com/cli/commands/npm-star>.

- Star a public package from the default registry:

`npm star {{pakket_naam}}`

- Star a package within a specific scope:

`npm star @{{scope}}/{{pakket_naam}}`

- Star a package from a specific registry:

`npm star {{pakket_naam}} --registry={{registry_url}}`

- Star a private package that requires authentication:

`npm star {{pakket_naam}} --auth-type={{legacy|oauth|web|saml}}`

- Star a package by providing an OTP for two-factor authentication:

`npm star {{pakket_naam}} --otp={{otp}}`

- Star a package with detailed logging:

`npm star {{pakket_naam}} --loglevel=verbose`

- List all your starred packages:

`npm star --list`

- List your starred packages from a specific registry:

`npm star --list --registry={{registry_url}}`
