return {
    LrSdkVersion        = 3.0,
    LrSdkMinimumVersion = 3.0,
    LrToolkitIdentifier = 'de.wendlandnet.photo.lightroom.GmxPublishService',
    LrPluginName        = LOC '$$$/GMXPublishService/PluginName=GMX Fotoalbum Publish Service',
    VERSION             = {
        major    = 0,
        minor    = 1,
        revision = 1,
        build    = 1,
    },

    LrExportServiceProvider = {
        title = 'GMX Fotoalbum',
        file  = 'PublishServiceProvider.lua',
    },

    LrExportMenuItems = {
        title = "GMX Login",
        file = "User.lua",
    },
}
