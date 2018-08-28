# FOP2KPXC

When I realized I could use [KeePassXC](https://keepassxc.org/) to handle Two-Factor Authentications (2FA) I got the urgency to extract my keys from the files exported from [FreeOTP+](https://github.com/helloworld1/FreeOTPPlus) (available on [Google Play](https://play.google.com/store/apps/details?id=org.liberty.android.freeotpplus) and [F-Droid](https://f-droid.org/en/packages/org.liberty.android.freeotpplus/) stores).

## Step-by-step usage

1. Export data from FreeOTP+ (touch on vertical ellipsis "⋮" on top of the screen, "Export" and choose a file name and a location where to store it);
1. Transfer the exported file to your computer;
1. Run `freeotp_fetch_keys.py <your_saved_file.json>` contained in this repository; it will attempt to identify each TOTP key with a friendly name. If you see any `<unknown>` labels, please contribute to this project;
1. Copy the string that follows the label;
1. Open KeePassXC file where to place the access credentials;
1. Right click over the entry to which we want to add 2FA and choose: "Time-based one-time password" > "Set up TOTP...";
1. Paste the copied value from step 4 into "Key" field and choose "Default RFC 6238 token settings";
1. Validate that both FreeOTP+ and KeePassXC (right-click, "Time-based one-time password" > "Show TOTP") show the same values.

## Credits

This project is available under MIT License and it's based on a [GIST](https://gist.github.com/jleclanche/a1dd8d88b8e41718e42ac1be52ac7829) published by @jleclanche.
